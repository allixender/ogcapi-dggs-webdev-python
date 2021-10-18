from dggs_api_server import config_fields as f

from dggs_api_server.models.collection_list import CollectionList
from dggs_api_server.models.collection import Collection
from dggs_api_server.models.link import Link  # noqa: F401,E501

import sqlite3

db = None

if f["driver"] == "clickhouse_driver":
    import dggs_api_server.dataaccess.clickhouse_dao as dbdao
    from dggs_api_server.dataaccess.clickhouse_dao import db

elif f["driver"] == "sqlite3":
    import dggs_api_server.dataaccess.sqlite_dao as dbdao
    from dggs_api_server.dataaccess.sqlite_dao import db

else:
    raise ImportError("no suitable db dao configured")


def capabilities_collections_get():
    return dbdao.capabilities_collections_get(db)


def dggs_access_collections_collection_id_describe_get(collection_id):
    return dbdao.dggs_access_collections_collection_id_describe_get(db, collection_id)


def dggs_access_collections_collection_id_zone_get(collection_id):
    return dbdao.dggs_access_collections_collection_id_zone_get(db, collection_id)


def dggs_access_collections_collection_id_zones_get(
    collection_id, resolution, bbox=None, zone_id_list=None, limit=None
):
    return dbdao.dggs_access_collections_collection_id_zones_get(
        db, collection_id, resolution, bbox=None, zone_id_list=None, limit=None
    )
