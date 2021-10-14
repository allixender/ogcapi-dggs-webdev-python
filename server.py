#!/usr/bin/env python3
import connexion
import os
from dggs_api_server import encoder

# We need an env var named TABLES_CONFIG
# this TABLES_CONFIG var should hold the path to a file# based on the
# tables.template.conf wich holds the access info to the clickhouse database server


def main():
    specification_dir = "./dggs_api_server/swagger"
    app = connexion.App(__name__, specification_dir=specification_dir)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api(
        "swagger-0.0.4.yaml",
        arguments={"title": "WIP: OGC API DGGS ZoneQuery - process style"},
        pythonic_params=True,
    )
    app.run(port=8080)


if __name__ == "__main__":
    main()
