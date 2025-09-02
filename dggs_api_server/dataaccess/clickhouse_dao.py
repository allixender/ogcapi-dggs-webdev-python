from dggs_api_server import config_fields as f

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
        "SELECT table_name, dggs_type, resolutions, variables, description, meta_url, extent, date_loaded FROM dggs_catalog",
        with_column_types=False,
        columnar=False,
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

        c_list.append(c)

    return c_list


def catalog_describe_id_get(db, collection_id):
    rs = db.ch_client.execute(
        "SELECT table_name, dggs_type, resolutions, variables, description, meta_url, extent, date_loaded FROM dggs_catalog where table_name = {}".format(
            collection_id
        ),
        with_column_types=False,
        columnar=False,
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

        return c
    return None
