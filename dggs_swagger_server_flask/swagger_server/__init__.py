from pyhocon import ConfigFactory
from clickhouse_driver import Client as ChClient
import os


def get_connection_details():

    TABLES_CONFIG = os.environ.get("TABLES_CONFIG")

    if not TABLES_CONFIG:
        raise ValueError("No TABLES_CONFIG set for Flask application")

    conf = ConfigFactory.parse_file(TABLES_CONFIG)

    database = conf.get("db.database")
    host = conf.get_string("db.host")
    port = conf["db.port"]  #
    user = conf["db"]["user"]
    password = conf.get_config("db")["password"]
    secure = conf.get_bool("db.secure")
    verify = conf.get_bool("db.verify")
    compression = conf.get_bool("db.compression")

    return {
        "database" : database,
        "host" : host,
        "port" : port,
        "user" : user,
        "password" : password,
        "secure":secure,
        "verify":verify,
        "compression":compression

    }

config_fields = get_connection_details()
