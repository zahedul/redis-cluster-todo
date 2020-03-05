import redis
import sys

MASTER_01 = '192.168.11.101'
SLAVE_01 = '192.168.11.111'
SLAVE_02 = '192.168.11.112'
PASSWORD = 'qweqwe123'

def ping_master():
    r = redis.Redis(host=MASTER_01, port=6379, password=PASSWORD)
    result = r.ping()
    return result

def ping_slave1():
    r = redis.Redis(host=SLAVE_01, port=6379, password=PASSWORD)
    result = r.ping()
    return result

def ping_slave2():
    r = redis.Redis(host=SLAVE_02, port=6379, password=PASSWORD)
    result = r.ping()
    return result

def set_master(key, value):
    r = redis.Redis(host=MASTER_01, port=6379, password=PASSWORD)
    result = r.set(key, value)
    return result

def set_slave1(key, value):
    r = redis.Redis(host=SLAVE_01, port=6379, password=PASSWORD)
    result = r.set(key, value)
    return result

def set_slave2(key, value):
    r = redis.Redis(host=SLAVE_02, port=6379, password=PASSWORD)
    result = r.set(key, value)
    return result

def get_master(key):
    r = redis.Redis(host=MASTER_01, port=6379, password=PASSWORD)
    result = r.get(key)
    return result

def get_slave1(key):
    r = redis.Redis(host=SLAVE_01, port=6379, password=PASSWORD)
    result = r.get(key)
    return result

def get_slave2(key):
    r = redis.Redis(host=SLAVE_02, port=6379, password=PASSWORD)
    result = r.get(key)
    return result



def main(*args, **kwargs):
    cmd = kwargs['cmd']
    server = kwargs['server']
    
    if cmd == 'ping':
        if server == 'master':
            print(ping_master())
        elif server == 'slave1':
            print(ping_slave1())
        elif server == 'slave2':
            print(ping_slave2())
    elif cmd == 'set':
        key = kwargs['key']
        value = kwargs['value'] 
        if server == 'master':
            print(set_master(key, value))
        elif server == 'slave1':
            print(set_slave1(key, value))
        elif server == 'slave2':
            print(set_slave2(key, value))
    elif cmd == 'get':
        key = kwargs['key']
        if server == 'master':
            print(get_master(key))
        elif server == 'slave1':
            print(get_slave1(key))
        elif server == 'slave2':
            print(get_slave2(key))




if __name__ == "__main__":
    data = sys.argv[1:]
    if data[0] == 'set':
        main(cmd=data[0], server=data[1], key=data[2], value=data[3])
    elif data[0] == 'get':
        main(cmd=data[0], server=data[1], key=data[2])
    else:
        main(cmd=data[0], server=data[1])
    