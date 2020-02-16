# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HousePriceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    province = scrapy.Field()  # 省
    city = scrapy.Field()  # 市
    properties = scrapy.Field()  # 楼盘名称
    alias = scrapy.Field()  # 楼盘别名
    date = scrapy.Field()  # 日期
    area = scrapy.Field()  # 区域
    address = scrapy.Field()  # 地址
    avg_unit_price = scrapy.Field()  # 每平米平均价格
    avg_total_price = scrapy.Field()  # 平均总价格


class HouseDetailItem(scrapy.Item):
    # 基本信息
    b_property_type = scrapy.Field()  # 物业类型
    b_reference_price = scrapy.Field()  # 参考价格
    b_project_characteristics = scrapy.Field()  # 项目特色
    b_area_address = scrapy.Field()  # 区域地址
    b_real_estate_address = scrapy.Field()  # 楼盘地址
    b_sales_office_address = scrapy.Field()  # 售楼处地址
    b_developers = scrapy.Field()  # 开发商

    # 楼盘纪事
    property_chronicle = scrapy.Field()  # 楼盘纪事 存json字符串
    staging_information = scrapy.Field()  # 分期信息 存json字符串

    # 规划信息 Planning information
    p_building_type = scrapy.Field()  # 建筑类型
    p_greening_rate = scrapy.Field()  # 绿化率
    p_area = scrapy.Field()  # 占地面积
    p_volume_rate = scrapy.Field()  # 容积率
    p_construction_area = scrapy.Field()  # 建筑面积
    p_type_of_property = scrapy.Field()  # 物业类型
    p_planning_households = scrapy.Field()  # 规划户数
    p_property_rights = scrapy.Field()  # 产权年限
    p_property_type = scrapy.Field()  # 楼盘户型

    # 售卖资格 Eligibility for sale
    eligibility_for_sale = scrapy.Field()  # 售卖资格 json数组

    # 配套信息 Supporting information
    s_property_company = scrapy.Field()  # 物业公司
    s_parking_ratio = scrapy.Field()  # 车位配比
    s_property_costs = scrapy.Field()  # 物业费
    s_heating_method = scrapy.Field()  # 供暖方式
    s_water_method = scrapy.Field()  # 供水方式
    s_power_method = scrapy.Field()  # 供电方式
    s_parking_space = scrapy.Field()  # 车位
    s_peripheral_planning = scrapy.Field()  # 周边规划
