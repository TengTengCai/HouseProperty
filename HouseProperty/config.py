import logging

import yaml

logger = logging.getLogger(__name__)

BASE_INFO_KEYS = {
    '物业类型': 'b_property_type',
    '参考价格': 'b_reference_price',
    '项目特色': 'b_project_characteristics',
    '区域地址': 'b_area_address',
    '楼盘地址': 'b_real_estate_address',
    '售楼处地址': 'b_sales_office_address',
    '开发商': 'b_developers',
}
PLANNING_INFO_KEY

def load_config():
    with open('config.yml', encoding='UTF-8') as f:
        try:
            config = yaml.safe_load(f)
        except Exception as e:
            logger.error("Load Config Error: {}".format(e))
    return config
