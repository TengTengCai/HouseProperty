import pymongo
import redis as redis

from HouseProperty.config import load_config

conf = load_config()
redis_conf = conf['redis']
mongo_conf = conf['mongo']
pool = redis.ConnectionPool(
    host=redis_conf['host'],
    port=redis_conf['port'],
    password=redis_conf['password'],
    db=redis_conf['db'],
    max_connections=10
)


def get_redis_pool():
    return redis.Redis(connection_pool=pool, decode_responses=True)


class MongoConn(object):
    def __init__(self, host="", port="", user="", password="", db=""):
        if host:
            self._host = host
        else:
            self._host = mongo_conf['host']
        if port:
            self._port = port
        else:
            self._port = mongo_conf['port']
        if user:
            self._user = user
        else:
            self._user = mongo_conf['user']
        if password:
            self._password = password
        else:
            self._password = mongo_conf['password']
        if db:
            self._db_name = db
        else:
            self._db_name = mongo_conf['db']
        self._client = pymongo.MongoClient(
            self._host,
            self._port,
            username=self._user,
            password=self._password)
        self._db = self._client[self._db_name]

    def get_house_price_collection(self):
        return self._db['housePrice']

    def get_house_detail_collection(self):
        return self._db['houseDetail']
