# -*- coding: utf-8 -*-
import datetime
import hashlib
import logging
from urllib.parse import urljoin

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from HouseProperty import settings
from HouseProperty.connection import get_redis_pool
from HouseProperty.items import HousePriceItem, HouseDetailItem

logger = logging.getLogger(__name__)


class LianjiaSpider(CrawlSpider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['http://lianjia.com/']

    rules = (
        # Rule(LinkExtractor(allow=r'loupan/[a-z_]*?/$'), callback='parse_house_price_item', follow=True),
        Rule(LinkExtractor(allow=r'loupan/[a-z_]*?/xiangqing/$'), callback='parse_house_detail_item', follow=True),
    )

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.redis_conn = get_redis_pool()
        self.m = hashlib.md5()
        self.date = datetime.datetime.now().strftime('%Y-%m-%d')

    def parse_house_price_item(self, response):
        url = str(response.url).encode('utf-8')
        self.m.update(url)
        url_md5 = self.m.hexdigest()
        old_date = self.redis_conn.hget(settings.HOUSE_PRICE_URL_HASH, url_md5)
        if old_date == self.date:
            return
        self.redis_conn.hset(settings.HOUSE_PRICE_URL_HASH, url_md5, self.date)
        item = HousePriceItem()
        item['city'] = response.xpath('//a[@class="s-city"]/text()').get()
        properties = response.xpath('//h2[@class="DATA-PROJECT-NAME"]/text()').get()
        if properties:
            item['properties'] = properties
        else:
            for href in response.xpath('//a/@href').getall():
                yield scrapy.Request(response.urljoin(href))
        try:
            alias = response.xpath('//div[@class="other-name"]/text()').get()
            if alias is None:
                item['alias'] = ''
            else:
                item['alias'] = str(alias).strip().split('：')[1]
        except Exception as e:
            logger.error("parser alias have error: {}".format(e))
            item['alias'] = ''
        item['date'] = self.date
        area = response.xpath('//div[@class="breadcrumbs"]//a[4]/text()').get()
        try:
            item['area'] = str(area).split('楼盘')[0]
        except Exception as e:
            logger.error("parser area have error: {}".format(e))
            item['area'] = area
        item['address'] = response.xpath(
            '//div[@class="info-wrap"]//ul[@class="info-list"]//li[@class="info-item"][1]//span[@class="content"]/'
            'text()').get()
        item['avg_unit_price'] = response.xpath(
            '//div[@class="top-info"]//div[@class="price"]/span[@class="price-number"][1]/text()').get()
        total_price = response.xpath(
            '//div[@class="top-info "]//span[@class="price-number"][2]/text()').get()
        try:
            item['avg_total_price'] = int(total_price) * 10000
        except Exception as e:
            logger.error("parser avg_total_price have error: {}".format(e))
            item['avg_total_price'] = 0
        yield item

    def parse_house_detail_item(self, response):
        url = response.url
        item = HouseDetailItem()
        self.m.update(url)
        url_md5 = self.m.hexdigest()
        if self.redis_conn.sismember(settings.HOUSE_DETAIL_URL_SET, url_md5):
            return
        self.redis_conn.sadd(settings.HOUSE_DETAIL_URL_SET, url_md5)
        item['properties'] = response.xpath('//div[@class="fl l-txt"]//a[5]/text()').get()
        base_infos = response.xpath('//div[@class="big-left fl"]//ul[@class="x-box"][1]//li').getall()
        for i, v in enumerate(base_infos):
            value = v.xpath('./span//text()').getall()
            value = ''.join(value[1:]).strip()
        yield item
