from dggs_api_server import config_fields as f

from dggs_api_server.models.collection_list import CollectionList
from dggs_api_server.models.collection import Collection
from dggs_api_server.models.link import Link  # noqa: F401,E501

import sqlite3


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
        c = Collection(
            id=row[0],
            dggs_id=row[1],
            title=row[0],
            description=row[4],
            resolutions=row[2],
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
        c = Collection(
            id=row[0],
            dggs_id=row[1],
            title=row[0],
            description=row[4],
            resolutions=row[2],
            links=links,
        )
        return c
    return None
