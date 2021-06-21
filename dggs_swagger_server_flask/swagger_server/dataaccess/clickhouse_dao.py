from clickhouse_driver import Client as ChClient
from swagger_server import config_fields as f

ch_client = ChClient(f['host'],
            user=f['user'],
            password=f['password'],
            secure=f['secure'],
            verify=f['verify'],
            database=f['database'],
            compression=f['compression'])
