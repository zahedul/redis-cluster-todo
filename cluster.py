from redis.sentinel import Sentinel
from redis import StrictRedis
import sys

def connect():
    server_1 = '192.168.11.101'
    server_2 = '192.168.11.111'
    server_3 = '192.168.11.112'
    password = 'qweqwe123'

    connection = Sentinel([(server_1, 26379), (server_2, 26379), (server_3, 26379)])
    host, port = connection.discover_master('redis-cluster')
    redis_client = StrictRedis(
        host=host,
        port=port,
        password=password
    )
    print(host)
    print(redis_client.set('city', 'feni'))

if __name__ == "__main__":
    connect()
    # master = connection.master_for('redis-cluster')
    # print(connection.discover_master('redis-cluster'))
    # print(master.ping())
    