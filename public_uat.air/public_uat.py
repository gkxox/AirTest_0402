# -*- encoding=utf8 -*-
__author__ = "gkxox"

from airtest.core.api import *
from airtest.core.api import using
using("variable.air")


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

import time
import random


auto_setup(__file__)

uat = "com.huawei.iretail.salesassistant.uat"

phone = str(random.randint(100000000,999999999))

# wake()
start_app(uat)

def login_uat():

    time.sleep(5)
    if poco(uat +':id/et_account').exists():
        poco(uat+ ':id/et_account').set_text('')
        poco(uat + ':id/et_account').set_text('isrptest14')
        poco(uat +':id/et_password').set_text('Pr0d1234!')
        poco(uat + ':id/btn_login').click()
        print('TRUE')
          

def add_potential():
    
    poco(uat + ':id/btn_add').click()
    poco(uat + ':id/et_name').set_text('Airtest')
    poco(uat + ':id/rb_sexMan').click()
    poco(uat + ':id/et_phone').set_text('10'+ phone)
    poco(uat + ':id/ra_item').click()
    
    poco(uat + ':id/tv_sale_person').click()
    touch(wait(Template(r"tpl1648834631352.png", record_pos=(-0.254, -0.093), resolution=(1080, 1920))))
    poco(uat + ':id/car_assign_confirm_btn').click()
    poco(uat + ':id/tv_next_follow_date').click()
    poco(uat + ':id/btn_confirm').click()
    poco(uat + ':id/btn_complete').click()
    
#     else:
#         poco(text='首页').click()
#         print("False")
            
# login_uat()
        
