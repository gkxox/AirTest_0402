# -*- encoding=utf8 -*-
__author__ = "gkxox"

from airtest.core.api import *
import json

auto_setup(__file__)

data = '''[

"env":{
    ["UAT":"com.huawei.iretail.salesassistant.uat"]

}

]'''


def parse_json():
    
    test_data = json.loads(data)
    print(test_data['env'])


