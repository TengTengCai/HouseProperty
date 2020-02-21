import logging

import yaml

logger = logging.getLogger(__name__)

BASE_INFO_KEYS = {
    '物业类型': 'b_property_type',
    '参考价格': 'b_reference_price',
    '项目特色': 'b_project_characteristics',
    '区域位置': 'b_area_address',
    '楼盘地址': 'b_real_estate_address',
    '售楼处地址': 'b_sales_office_address',
    '开发商': 'b_developers',
}
PLANNING_INFO_KEYS = {
    '建筑类型': 'p_building_type',
    '绿化率': 'p_greening_rate',
    '占地面积': 'p_area',
    '容积率': 'p_volume_rate',
    '建筑面积': 'p_construction_area',
    '物业类型': 'p_type_of_property',
    '规划户数': 'p_planning_households',
    '产权年限': 'p_property_rights',
    '楼盘户型': 'p_property_type',
}

SUPPORTING_INFO_KEYS = {
    '物业公司': 's_property_company',
    '车位配比': 's_parking_ratio',
    '物业费': 's_property_costs',
    '供暖方式': 's_heating_method',
    '供水方式': 's_water_method',
    '供电方式': 's_power_method',
    '车位': 's_parking_space',
    '周边规划': 's_peripheral_planning',
}


def load_config():
    with open('config.yml', encoding='UTF-8') as f:
        try:
            config = yaml.safe_load(f)
        except Exception as e:
            logger.error("Load Config Error: {}".format(e))
    return config
