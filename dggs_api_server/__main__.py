#!/usr/bin/env python3

import connexion
from flask_cors import CORS
from dggs_api_server import encoder

import logging
from logging.config import dictConfig


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

    app = connexion.App(__name__, specification_dir="./swagger/")
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api(
        "swagger.yaml",
        arguments={"title": "WIP: OGC API DGGS ZoneQuery - process style"},
        pythonic_params=True,
    )

    CORS(app.app)
    app.app.logger.info("I configured the flask logger!")
    app.run(port=8080)


if __name__ == "__main__":
    main()
