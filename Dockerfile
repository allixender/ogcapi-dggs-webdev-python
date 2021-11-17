FROM python:3.8-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements*.txt /usr/src/app/

RUN pip install --no-cache-dir connexion[swagger-ui]
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --no-cache-dir -r requirements-rhealpix.txt
# RUN pip3 install --no-cache-dir -r requirements-clickhouse.txt

COPY . /usr/src/app

RUN ln -s /usr/src/app/dggs_api_server/swagger/swagger-0.0.6a.yaml /usr/src/app/dggs_api_server/swagger/swagger.yaml

ENV TABLES_CONFIG /usr/src/app/tables.template.conf
ENV BASE_URL http://localhost:8080/dggs-api

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["server.py"]
