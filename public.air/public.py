# -*- encoding=utf8 -*-
__author__ = "gkxox"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# from airtest.core.api import using
using("variable.air")
from variable import * 

auto_setup(__file__)

def login_xcb():
    
    poco('com.bjcsxq.chat.carfriend:id/login_phone_et')
    
    poco('com.bjcsxq.chat.carfriend:id/login_phone_et').set_text(Login['username'])
    
    poco('com.bjcsxq.chat.carfriend:id/login_pwd_et').set_text(Login['password'])
    
    poco('com.bjcsxq.chat.carfriend:id/check').click()
    
    poco('com.bjcsxq.chat.carfriend:id/login_btn').click()
    
    poco('com.bjcsxq.chat.carfriend:id/btn_neg').click()
    
    
def login_xc():
    
    # 切换账号密码登录
    
    change_btn = poco('ctrip.android.login:id/tvLeftBtn')
    change_btn.wait_for_appearance()
    change_btn.click()
    
    # 输入手机号
    poco(text="境内手机号/用户名/邮箱/卡号").set_text('15895802308')
    
    # 输入密码
    keyevent('TAB')
    text('qq395264')
                                                               
    # 点击登录
    poco("ctrip.android.login:id/tvDoLogin").click()

    # 服务协议      
    if exists(Template(r"tpl1646473561507.png", record_pos=(-0.003, 0.022), resolution=(720, 1280))):
        touch(Template(r"tpl1646473609265.png", record_pos=(-0.001, 0.079), resolution=(720, 1280)))
        
def create_leads():
    
    touch((680,881))

poco.swipe((0.5,0.8),(0.5,0.1))


def login_salesassistant_UAT():
    
    if not poco('com.huawei.iretail.salesassistant.uat:id/tab_mine'):
        poco('com.huawei.iretail.salesassistant.uat:id/et_account').set_text('isrptest14')
        
        
    
    
