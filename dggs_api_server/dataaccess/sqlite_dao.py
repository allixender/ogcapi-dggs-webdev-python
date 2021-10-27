from dggs_api_server import config_fields as f

from dggs_api_server.models.collection_list import CollectionList
from dggs_api_server.models.link import Link  # noqa: F401,E501

from dggs_api_server.models.exception import (
    DggsException,
    DggsCollectionIdNotFoundError,
)  # noqa: E501
from dggs_api_server.models.zone_collection_geo_json import (
    ZoneCollectionGeoJSON,
)  # noqa: E501
from dggs_api_server.models.zone_geo_json import ZoneGeoJSON  # noqa: E501
from dggs_api_server.models.dggsjson import DGGSJSON  # noqa: E501

from dggs_api_server.dataaccess import dggs_transform

import sqlite3

from flask import current_app, logging


class SqliteDB:
    def __init__(self):
        self.conn = sqlite3.connect(f["database"], check_same_thread=False)


db = SqliteDB()
db_where_clause_limit = 100
service_feature_limit = 5000


def catalog_get(db: SqliteDB):
    """
    0 `table_name` String,
    1 `dggs_type` String,
    2 `extent` Array(Int32),
    `base_resolution` UInt16,
    4 `resolutions` Array(UInt16),
    5 `variables` Array(String),
    6 `description` String,
    7 `meta_url` String,
    `date_loaded` DateTime,
    `date_updated` DateTime
    """
    cursor = db.conn.cursor()
    rs = cursor.execute(
        "SELECT table_name, dggs_type, resolutions, variables, description, meta_url, extent, date_loaded FROM dggs_catalog"
    )
    c_list = []
    field_names = [description[0] for description in rs.description]

    for row in rs:
        tx = zip(field_names, row)
        c = dict(tx)

        links = [c["meta_url"]] if c["meta_url"] is not None else []
        resolutions = [
            int(x) for x in c["resolutions"].split(":") if c["resolutions"] is not None
        ]
        variables = c["variables"].split(":") if c["variables"] is not None else []
        extent = [float(x) for x in c["extent"].split(",") if c["extent"] is not None]

        c.update({"variables": variables})
        c.update({"extent": extent})
        c.update({"resolutions": resolutions})
        c.update({"links": links})

        print(str(c))
        c_list.append(c)

    return c_list


def catalog_describe_id_get(db, collection_id):
    rs = db.conn.execute(
        "SELECT table_name, dggs_type, resolutions, variables, description, meta_url, extent, date_loaded FROM dggs_catalog where table_name = '{}'".format(
            collection_id
        )
    )
    field_names = [description[0] for description in rs.description]
    for row in rs:
        tx = zip(field_names, row)
        c = dict(tx)

        links = [c["meta_url"]] if c["meta_url"] is not None else []
        resolutions = [
            int(x) for x in c["resolutions"].split(":") if c["resolutions"] is not None
        ]
        variables = c["variables"].split(":") if c["variables"] is not None else []
        extent = [float(x) for x in c["extent"].split(",") if c["extent"] is not None]

        c.update({"variables": variables})
        c.update({"extent": extent})
        c.update({"resolutions": resolutions})
        c.update({"links": links})

        print(str(c))
        return c
    return None


def build_dggs_json_feature(
    names, row, ftype="Feature", cell_id_name="cell_id", ignore_fields=["parent_ids"]
):
    data = dict(zip(names, row))

    d = {
        "geometry": [data[cell_id_name]],
        "id": data[cell_id_name],
        "properties": {},
        "type": ftype,
    }
    [
        d["properties"].update({k: v})
        for (k, v) in data.items()
        if k not in [cell_id_name] + ignore_fields
    ]
    return d


def dggs_access_collections_collection_id_zone_get(db, collection_id, zone_id):
    rs = db.conn.execute(
        "SELECT * FROM {} where cell_id = '{}' limit 1".format(collection_id, zone_id)
    )
    names = [description[0] for description in rs.description]

    that_row = rs.fetchone()
    if not that_row is None:

        d = build_dggs_json_feature(names, that_row)

        # if media_type_request == "application/geo+json":
        #     return ZoneGeoJSON(type="Feature", geometry=dggs_transform.to_geojson(d['geometry']), properties=d['properties'], id=d['id'], links=[], resolution=dggs_transform.get_resolution(d['id'])))

        return DGGSJSON(
            type="Feature",
            geometry=d["geometry"],
            id=d["id"],
            properties=d["properties"],
            links=[],
        )
    else:
        return None


def dggs_access_collections_collection_id_zones_get(
    db, collection_id, resolution, bbox=None, zone_id_list=None, limit=None
):
    params = f"c {collection_id}, r {resolution}, b {bbox}, z {zone_id_list}, l {limit}"
    current_app.logger.info(params)

    dggs_info = dggs_access_collections_collection_id_describe_get(db, collection_id)
    if dggs_info is None:
        return None

    dggs_type = dggs_info.dggs_id

    zone_selection_list = []
    has_parents = False

    if zone_id_list is not None and isinstance(zone_id_list, list):
        target_zone_id_list = []
        if len(zone_id_list) > db_where_clause_limit:
            # reduce via parents
            parent_ids = dggs_transform.get_parents_max_list(
                dggs_type, zone_id_list, db_where_clause_limit
            )
            target_zone_id_list = list(parent_ids)
            has_parents = True
        else:
            target_zone_id_list = zone_id_list
        zone_selection_list = zone_selection_list + target_zone_id_list

    if bbox is not None:
        minx, miny, maxx, maxy = bbox
        area_json = {
            "type": "Polygon",
            "coordinates": [
                [[miny, minx], [miny, maxx], [maxy, maxx], [maxy, minx], [miny, minx]]
            ],
        }
        zone_id_list_from_fill = dggs_transform.fill_area(
            dggs_type, area_json, resolution
        )
        target_zone_id_list = []
        if len(zone_id_list_from_fill) > db_where_clause_limit:
            # reduce via parents
            parent_ids = dggs_transform.get_parents_max_list(
                dggs_type, zone_id_list_from_fill, db_where_clause_limit
            )
            target_zone_id_list = list(parent_ids)
            has_parents = True
        else:
            target_zone_id_list = list(zone_id_list_from_fill)
        zone_selection_list = zone_selection_list + target_zone_id_list

    zone_clause = ""
    if len(zone_selection_list) > 0:

        # (parent_ids like '%8511346ffffffff%' or parent_ids like '%85113473fffffff%');
        if has_parents:
            zones_str = [f"parent_ids like '%{zone}%'" for zone in zone_selection_list]
            zone_clause = " or ".join(zones_str)
            zone_clause = f" AND ( {zone_clause} )"
        else:
            zones_str = [f"'{zone}'" for zone in zone_selection_list]
            zone_clause = ",".join(zones_str)
            zone_clause = f" AND cell_id IN ( {zone_clause} )"

    limit_val = service_feature_limit if limit is None else limit
    if limit is not None and limit > service_feature_limit:
        limit_val = service_feature_limit

    limit_str = "LIMIT {}".format(int(limit_val))

    sql = "SELECT * FROM {} where resolution = {} {} {}".format(
        collection_id, int(resolution), zone_clause, limit_str
    )
    current_app.logger.info(sql)

    rs = db.conn.execute(sql)

    names = [description[0] for description in rs.description]

    results = []

    for row in rs:
        d = build_dggs_json_feature(names, row)
        dz = DGGSJSON(
            type="Feature",
            geometry=d["geometry"],
            id=d["id"],
            properties=d["properties"],
            links=[],
        )
        results.append(dz)

    return ZoneCollectionGeoJSON(type="FeatureCollection", features=results)
