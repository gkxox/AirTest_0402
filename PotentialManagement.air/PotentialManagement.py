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
    poco(uat + ':id/btn_add').click()
    poco(uat + ':id/et_name').set_text('Airtest')
    poco(uat + ':id/rb_sexMan').click()
    poco(uat + ':id/et_phone').set_text('10'+ phone)
    poco(uat + ':id/ra_item').click()
    
    poco(uat + ':id/tv_sale_person').click()
    touch(wait(Template(r"tpl1648833203008.png", record_pos=(-0.271, -0.088), resolution=(1080, 1920))))
    poco(uat + ':id/car_assign_confirm_btn').click()
    poco(uat + ':id/tv_next_follow_date').click()
    poco(uat + ':id/btn_confirm').click()
    poco(uat + ':id/btn_complete').click()
    
    result = poco(uat + ':id/tv_right').click()
    
       
test_03_create_potential()
