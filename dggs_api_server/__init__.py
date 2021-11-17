from pyhocon import ConfigFactory
import os


def get_base_url():
    BASE_URL = "http://localhost:8080/dggs-api"
    try:
        BASE_URL = os.environ.get("BASE_URL")
    except KeyError:
        print("No BASE_URL env var set for Flask application, will be localhost")
    return BASE_URL


def get_connection_details():

    TABLES_CONFIG = os.environ.get("TABLES_CONFIG")

    if not TABLES_CONFIG:
        raise ValueError("No TABLES_CONFIG env var set for Flask application")

    conf = ConfigFactory.parse_file(TABLES_CONFIG)

    driver = conf.get("db.driver")

    if driver == "clickhouse_driver":
        database = conf.get("db.clickhouse.database")
        host = conf.get_string("db.clickhouse.host")
        port = conf["db.clickhouse.port"]
        user = conf["db.clickhouse"]["user"]
        password = conf.get_config("db.clickhouse")["password"]
        secure = conf.get_bool("db.clickhouse.secure")
        verify = conf.get_bool("db.clickhouse.verify")
        compression = conf.get_bool("db.clickhouse.compression")

        return {
            "driver": driver,
            "database": database,
            "host": host,
            "port": port,
            "user": user,
            "password": password,
            "secure": secure,
            "verify": verify,
            "compression": compression,
        }

    elif driver == "psycopg2":
        database = conf.get("db.postgres.database")
        schema = conf.get_bool("db.postgres.schema")
        host = conf.get_string("db.postgres.host")
        port = conf["db.postgres.port"]
        user = conf["db.postgres"]["user"]
        password = conf.get_config("db.postgres")["password"]
        ssl = conf.get_bool("db.postgres.ssl")

        return {
            "driver": driver,
            "database": database,
            "host": host,
            "port": port,
            "user": user,
            "password": password,
            "ssl": ssl,
            "schema": schema,
        }

    elif driver == "sqlite3":
        database = conf.get("db.sqlite.database")

        return {"driver": driver, "database": database}


config_fields = get_connection_details()
