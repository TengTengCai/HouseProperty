import pymongo
import redis as redis
from scrapy.settings import Settings

from HouseProperty.config import load_config

conf = load_config()
redis_conf = conf['REDIS']
mongo_conf = conf['MONGO']
email_conf = Settings(conf['E-MAIL'])
pool = redis.ConnectionPool(
    host=redis_conf['HOST'],
    port=redis_conf['PORT'],
    password=redis_conf['PASSWORD'],
    db=redis_conf['DB'],
    max_connections=10
)


def get_redis_pool():
    return redis.Redis(connection_pool=pool, decode_responses=True)


class MongoConn(object):
    def __init__(self, host="", port="", user="", password="", db=""):
        if host:
            self._host = host
        else:
            self._host = mongo_conf['HOST']
        if port:
            self._port = port
        else:
            self._port = mongo_conf['PORT']
        if user:
            self._user = user
        else:
            self._user = mongo_conf['USER']
        if password:
            self._password = password
        else:
            self._password = mongo_conf['PASSWORD']
        if db:
            self._db_name = db
        else:
            self._db_name = mongo_conf['DB']
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

    def close_client(self):
        self._client.close()
