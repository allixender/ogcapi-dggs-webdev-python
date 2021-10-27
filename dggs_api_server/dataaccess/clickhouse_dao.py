from dggs_api_server import config_fields as f

from dggs_api_server.models.collection_list import CollectionList
from dggs_api_server.models.catalog_entry import CatalogEntry  # noqa: E501
from dggs_api_server.models.link import Link  # noqa: F401,E501

from flask import current_app, logging

from clickhouse_driver import Client as ChClient


class ClickhouseDB:
    def __init__(self):
        self.ch_client = ChClient(
            f["host"],
            user=f["user"],
            password=f["password"],
            secure=f["secure"],
            verify=f["verify"],
            database=f["database"],
            compression=f["compression"],
        )


db = ClickhouseDB()


def catalog_get(db: ClickhouseDB):
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
    rs = db.ch_client.execute(
        "SELECT table_name, dggs_type, resolutions, variables, description, meta_url FROM dggs_catalog",
        with_column_types=False,
        columnar=False,
    )
    c_list = []
    for row in rs:
        c = CatalogEntry(
            id=row[0],
            dggs_id=row[1],
            title=row[0],
            description=row[4],
            resolutions=row[2],
            links=list(row[5]),
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


def catalog_describe_id_get(db, collection_id):
    rs = db.ch_client.execute(
        "SELECT table_name, dggs_type, resolutions, variables, description, meta_url FROM dggs_catalog where table_name = {}".format(
            collection_id
        ),
        with_column_types=False,
        columnar=False,
    )
    for row in rs:
        c = CatalogEntry(
            id=row[0],
            dggs_id=row[1],
            title=row[0],
            description=row[4],
            resolutions=row[2],
            links=list(row[5]),
        )
        return c
    return None
