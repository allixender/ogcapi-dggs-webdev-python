#!/usr/bin/env python3
import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir=r'C:\dev\build\test_projects\ogcapi-discrete-global-grid-systems\workdir\swagger_server\swagger')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'WIP: OGC API DGGS ZoneQuery - process style'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
