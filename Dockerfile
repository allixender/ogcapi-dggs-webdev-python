FROM python:3.8-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt
# RUN pip3 install --no-cache-dir -r requirements-clickhouse.txt

COPY . /usr/src/app

ENV TABLES_CONFIG /usr/src/app/tables.template.conf

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "dggs_api_server"]
