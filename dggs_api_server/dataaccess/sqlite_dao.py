from dggs_api_server import config_fields as f

from dggs_api_server.models.collection_list import CollectionList
from dggs_api_server.models.collection import Collection
from dggs_api_server.models.link import Link  # noqa: F401,E501

from dggs_api_server.models.collection import Collection  # noqa: E501
from dggs_api_server.models.exception import (
    DggsException,
    DggsCollectionIdNotFoundError,
)  # noqa: E501
from dggs_api_server.models.zone_collection_geo_json import (
    ZoneCollectionGeoJSON,
)  # noqa: E501
from dggs_api_server.models.zone_geo_json import ZoneGeoJSON  # noqa: E501

import sqlite3

from dggs_api_server.dataaccess import dggs_transform


class SqliteDB:
    def __init__(self):
        self.conn = sqlite3.connect(f["database"], check_same_thread=False)


db = SqliteDB()


def capabilities_collections_get(db: SqliteDB):
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
    rs = db.conn.execute(
        "SELECT table_name, dggs_type, resolutions, variables, description, meta_url FROM dggs_catalog"
    )
    c_list = []
    for row in rs:
        links = [row[5]] if row[5] is not None else []
        resolutions = row[2].split(":") if row[2] is not None else []

        c = Collection(
            id=row[0],
            dggs_id=row[1],
            title=row[0],
            description=row[4],
            resolutions=resolutions,
            links=links,
        )
        c_list.append(c)

    links = [
        Link(
            {
                "href": "http://data.example.org/dggs.json",
                "rel": "self",
                "title": "this document",
                "type": "application/json",
            }
        ),
        Link(
            {
                "href": "http://data.example.org/dggs.html",
                "rel": "alternate",
                "title": "this document as HTML",
                "type": "text/html",
            }
        ),
    ]

    cl = CollectionList(links=links, dggs_list=c_list)
    return cl


def dggs_access_collections_collection_id_describe_get(db, collection_id):
    rs = db.conn.execute(
        "SELECT table_name, dggs_type, resolutions, variables, description, meta_url FROM dggs_catalog where table_name = '{}'".format(
            collection_id
        )
    )
    for row in rs:
        links = [row[5]] if row[5] is not None else []
        resolutions = row[2].split(":") if row[2] is not None else []

        c = Collection(
            id=row[0],
            dggs_id=row[1],
            title=row[0],
            description=row[4],
            resolutions=resolutions,
            links=links,
        )
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


def dggs_access_collections_collection_id_zone_get(db, collection_id):
    rs = db.conn.execute("SELECT * FROM {} limit 1".format(collection_id))
    names = [description[0] for description in rs.description]

    that_row = rs.fetchone()
    if not that_row is None:

        d = build_dggs_json_feature(names, that_row)

        return ZoneGeoJSON(d)
    else:
        return None


def dggs_access_collections_collection_id_zones_get(
    db, collection_id, resolution, bbox=None, zone_id_list=None, limit=None
):
    dggs_info = dggs_access_collections_collection_id_describe_get(db, collection_id)
    if dggs_info is None:
        return None

    limit_val = 100 if limit is None else limit
    limit_str = "LIMIT {}".format(limit_val)

    zone_selection_list = []
    has_parents = False

    if not zone_id_list is None and isinstance(zone_id_list, list):
        target_zone_id_list = []
        if len(zone_id_list) > 100:
            # reduce via parents
            print(zone_id_list)
            has_parents = True
        else:
            target_zone_id_list = zone_id_list
        zone_selection_list = zone_selection_list + target_zone_id_list

    if not bbox is None:
        minx, miny, maxx, maxy = bbox
        area_json = {
            "type": "Polygon",
            "coordinates": [
                [[miny, minx], [miny, maxx], [maxy, maxx], [maxy, minx], [miny, minx]]
            ],
        }
        zone_id_list_from_fill = dggs_transform.fill_area(
            dggs_info.dggs_id, area_json, resolution
        )
        target_zone_id_list = []
        if len(zone_id_list_from_fill) > 100:
            # reduce via parents
            print(zone_id_list_from_fill)
            has_parents = True
        else:
            target_zone_id_list = zone_id_list_from_fill
        zone_selection_list = zone_selection_list + target_zone_id_list

    zone_clause = ""
    if len(zone_selection_list) > 0:
        zone_clause = ",".join(f"'{zone_selection_list}'")

        if has_parents:
            zone_clause = f" AND parent_ids IN ( {zone_clause} )"
        else:
            zone_clause = f" AND cell_ids IN ( {zone_clause} )"

    rs = db.conn.execute(
        "SELECT * FROM {} where resolution = {} {} {}".format(
            collection_id, resolution, zone_clause, limit_str
        )
    )

    names = [description[0] for description in rs.description]

    results = []

    for row in rs:
        d = build_dggs_json_feature(names, row)
        results.append(ZoneGeoJSON(d))

    return ZoneCollectionGeoJSON(type="FeatureCollection", features=results)
