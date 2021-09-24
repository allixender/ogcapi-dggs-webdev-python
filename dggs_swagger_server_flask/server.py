#!/usr/bin/env python3
import connexion

from swagger_server import encoder

# We need an env var named TABLES_CONFIG
# this TABLES_CONFIG var should hold the path to a file# based on the
# tables.template.conf wich holds the access info to the clickhouse database server

def main():
    app = connexion.App(__name__, specification_dir=r'.\swagger_server\swagger')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'WIP: OGC API DGGS ZoneQuery - process style'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
