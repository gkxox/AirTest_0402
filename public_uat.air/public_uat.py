# -*- encoding=utf8 -*-
__author__ = "gkxox"

from airtest.core.api import *
from airtest.core.api import using
using("variable.air")


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

import time


auto_setup(__file__)

uat = "com.huawei.iretail.salesassistant.uat"

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
          
    else:
        poco(text='首页').click()
#         print("False")
            
# login_uat()
        
