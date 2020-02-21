# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging

from HouseProperty.connection import MongoConn
from HouseProperty.items import HousePriceItem, HouseDetailItem

logger = logging.getLogger(__name__)


class HousePriceItemPipeline(object):
    def __init__(self):
        self._conn = MongoConn()
        self.house_price = self._conn.get_house_price_collection()

    def process_item(self, item, spider):
        if 'properties' not in item:
            return item
        if not item['properties']:
            return item
        if isinstance(item, HousePriceItem):
            logger.info(type(item))
            # logger.info(item['properties'])
            self.house_price.insert_one(dict(item))
        return item


class HouseDetailItemPipeline(object):
    def __init__(self):
        self._conn = MongoConn()
        self.house_detail = self._conn.get_house_detail_collection()

    def process_item(self, item, spider):
        if 'properties' not in item:
            return item
        if not item['properties']:
            return item
        if isinstance(item, HouseDetailItem):
            logger.info(type(item))
            # logger.info(item['properties'])
            self.house_detail.insert_one(dict(item))
        return item
