# -*- encoding=utf8 -*-
__author__ = "gkxox"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

from airtest.core.api import using
using("public.air")
from public import *

from airtest.report.report import simple_report

auto_setup(__file__)


from poco.drivers.ios import iosPoco
poco = iosPoco()

try:
    stop_app("com.bjcsxq.chat.carfriend")

    start_app("com.bjcsxq.chat.carfriend")

    # sleep(2)


    touch(wait(Template(r"tpl1646315768391.png", record_pos=(0.422, -0.831), resolution=(720, 1280))))
    # touch((658,38))
    # poco('android.widget.TextView').wait().click()

    poco("com.bjcsxq.chat.carfriend:id/mine_image").click()
    poco("com.bjcsxq.chat.carfriend:id/mine_head_img").click()



    if poco(text='您好！请登录').exists():

        login_xcb()

    else:
        print('已经登录')


    snapshot('登录成功.png')

    assert_equal(poco(text='没有昵称啊').get_text(),"没有昵称啊", "测试用户是否登录")

finally:
    simple_report(__file__)
