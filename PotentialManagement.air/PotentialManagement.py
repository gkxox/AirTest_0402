# -*- encoding=utf8 -*-
__author__ = "gkxox"

from airtest.core.api import *

from airtest.core.api import using

using("public_uat.air")
from public_uat import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

import time
import random

auto_setup(__file__)



uat = "com.huawei.iretail.salesassistant.uat"

phone = str(random.randint(100000000,999999999))

date = time.strftime('%Y-%m-%d')


# start_app(uat)
# login_uat()
    
def test_01_serah_with_id():
    login_uat()
        
    touch(wait(Template(r"tpl1648826519621.png", record_pos=(-0.347, 0.536), resolution=(1080, 1920))))
#     time.sleep(2)
    poco(uat + ':id/et_search').click()
    poco(uat + ':id/et_search').set_text('')
    text("12586999988", search=True)
    result = poco(uat + ':id/v_user_phone').get_text()
    assert_equal(result,'12586999988','按潜客电话查询')
    keyevent('BACK')

        
def test_02_searh_with_name():
    login_uat()
    touch(wait(Template(r"tpl1648826519621.png", record_pos=(-0.347, 0.536), resolution=(1080, 1920))))
    poco(uat + ':id/et_search').click()
    poco(uat + ':id/et_search').set_text('')
    text("Airtest01", search=True)
    assert_exists(Template(r"tpl1648831199695.png", record_pos=(-0.318, -0.26), resolution=(1080, 1920)))
    keyevent('BACK')
    

'''新增潜客'''
def test_03_create_potential():
    login_uat()
    touch(wait(Template(r"tpl1648826519621.png", record_pos=(-0.347, 0.536), resolution=(1080, 1920))))
#     time.sleep(2)
    add_potential()
    
    result = poco(uat + ':id/tv_right').get_text
#     assert_equal(result,'10'+phone,'测试新增潜客')
    for i in range(2):
        keyevent('BACK')
    
       
test_03_create_potential()
