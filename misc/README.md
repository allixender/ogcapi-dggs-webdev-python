# Testing Python code generated servers for ogcapi-discrete-global-grid-systems

See more for background: https://github.com/opengeospatial/ogcapi-discrete-global-grid-systems

## SwaggerHub API definition

The file xxx-dggs-zonequery.yml can be pasted into a SwaggerHub project to test the structure of the API An example such project is: https://app.swaggerhub.com/apis/rggibb/dggs-zonequery/

Subsequently, the Python projects here are based on the referenced YAML files to create server stubs.

## Sub project: dggs_dggs_api_server_flask

Generated from SwaggerHub via export function.

Comes with setup.py and some fixes/adjustments so that the base scaffold runs now. Can be used to flesh out actual API functionality.

```shell
python setup.py install

python server.py
```

HTTP base url: http://localhost:8080/rggibb/dggs-zonequery/0.0.4/ui/

## Sub project: dggs_dggs_api_server_fastapi

Generated as a FastAPI/Pydantic code scaffold with [koxudaxi/fastapi-code-generator](https://github.com/koxudaxi/fastapi-code-generator)

Needs uvicorn or gunicorn to run the main:app.

```shell
cd fastapi-test/app

uvicorn main:app

# errors out, other types errors already fixed
collection_id: str = Path(..., alias='collectionId'),
   ^
SyntaxError: non-default argument follows default argument

```

## database notes

[clickhouse initial info](./misc/database.md)
