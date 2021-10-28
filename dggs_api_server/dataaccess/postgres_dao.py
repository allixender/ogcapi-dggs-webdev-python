from dggs_api_server import config_fields as f

import psycopg2


class PostgresDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            f"dbname={f['database']} user={f['user']} password={f['password']} host={f['host']} port={f['port']}"
        )
        self.schema = f["database"]
        self.ssl = f["ssl"]


db = PostgresDB()


def catalog_get(db: PostgresDB):
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

        return c
    return None
