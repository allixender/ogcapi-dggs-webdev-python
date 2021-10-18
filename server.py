#!/usr/bin/env python3
import connexion
from flask_cors import CORS
import os
import logging
from logging.config import dictConfig

from dggs_api_server import encoder

# We need an env var named TABLES_CONFIG
# this TABLES_CONFIG var should hold the path to a file# based on the
# tables.template.conf wich holds the access info to the clickhouse database server


def main():

    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
                }
            },
            "handlers": {
                "wsgi": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://flask.logging.wsgi_errors_stream",
                    "formatter": "default",
                }
            },
            "root": {"level": "INFO", "handlers": ["wsgi"]},
        }
    )

    specification_dir = "./dggs_api_server/swagger"
    app = connexion.App(__name__, specification_dir=specification_dir)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api(
        "swagger-0.0.6.yaml",
        arguments={"title": "WIP: OGC API DGGS ZoneQuery - process style"},
        pythonic_params=True,
    )

    CORS(app.app)
    app.app.logger.info("I configured the flask logger!")
    app.run(port=8080)


if __name__ == "__main__":
    main()
