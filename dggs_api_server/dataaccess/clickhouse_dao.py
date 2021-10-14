from clickhouse_driver import Client as ChClient
from dggs_api_server import config_fields as f

from dggs_api_server.models.collection_list import CollectionList
from dggs_api_server.models.collection import Collection
from dggs_api_server.models.link import Link  # noqa: F401,E501

class ClickhouseDB():
    def __init__(self):
        self.ch_client = ChClient(f['host'],
                    user=f['user'],
                    password=f['password'],
                    secure=f['secure'],
                    verify=f['verify'],
                    database=f['database'],
                    compression=f['compression'])

db = ClickhouseDB()


def capabilities_collections_get(db: ClickhouseDB):
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
    rs = db.ch_client.execute('SELECT table_name, dggs_type, resolutions, variables, description, meta_url FROM dggs_catalog',
        with_column_types=False, columnar=False)
    c_list = []
    for row in rs:
        c = Collection(id=row[0], dggs_id=row[1], title=row[0], description=row[4], resolutions=row[2], links=list(row[5]))
        c_list.append(c)

    d = {
          "dggs-list": [
            {
              "description": "The rHealPix DGGS",
              "id": "TB16-Pix",
              "links": [
                {
                  "href": "https://iopscience.iop.org/article/10.1088/1755-1315/34/1/012012/pdf",
                  "rel": "describedBy",
                  "title": "The rHealPix DGGS specification",
                  "type": "application/PDF"
                },
                {
                  "href": "http://data.example.org/dggs/rHealPix/zones",
                  "rel": "zones",
                  "type": "appplication/json"
                }
              ],
              "resolutions": [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14
              ],
              "title": "The Testbed16 DGGS based on rHealPix"
            },
            {
              "description": "The H3 DGGS",
              "id": "H3",
              "links": [
                {
                  "href": "https://eng.uber.com/h3/",
                  "rel": "describedBy",
                  "title": "The H3 specification",
                  "type": "text/html"
                },
                {
                  "href": "http://data.example.org/dggs/H3/zones",
                  "rel": "zones",
                  "type": "appplication/json"
                }
              ],
              "resolutions": [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16
              ],
              "title": "H3"
            }
          ],
          "links": [
            {
              "href": "http://data.example.org/dggs.json",
              "rel": "self",
              "title": "this document",
              "type": "application/json"
            },
            {
              "href": "http://data.example.org/dggs.html",
              "rel": "alternate",
              "title": "this document as HTML",
              "type": "text/html"
            }
          ]
        }

    links = [
                Link({
                  "href": "http://data.example.org/dggs.json",
                  "rel": "self",
                  "title": "this document",
                  "type": "application/json"
                }),
                Link({
                  "href": "http://data.example.org/dggs.html",
                  "rel": "alternate",
                  "title": "this document as HTML",
                  "type": "text/html"
                })
            ]

    cl = CollectionList(links = links, dggs_list = c_list)
    return cl


def dggs_access_collections_collection_id_describe_get(db, collection_id):
    rs = db.ch_client.execute('SELECT table_name, dggs_type, resolutions, variables, description, meta_url FROM dggs_catalog where table_name = {}'.format(collection_id),
        with_column_types=False, columnar=False)
    for row in rs:
        c = Collection(id=row[0], dggs_id=row[1], title=row[0], description=row[4], resolutions=row[2], links=list(row[5]))
        return c
    return None
