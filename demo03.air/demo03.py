# -*- encoding=utf8 -*-
__author__ = "gkxox"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

start_app('com.tencent.mm')

poco.scroll('up')

poco(text='华为旗舰店').click()

if exists(Template(r"tpl1646491191821.png", record_pos=(0.311, 0.66), resolution=(720, 1280))):
    touch(Template(r"tpl1646490687514.png", record_pos=(0.31, 0.66), resolution=(720, 1280)))

    touch(wait(Template(r"tpl1646490750276.png", record_pos=(0.001, 0.476), resolution=(720, 1280))))

    touch(wait(Template(r"tpl1646490810562.png", record_pos=(0.149, 0.787), resolution=(720, 1280))))
    
poco.scroll()

touch(wait(Template(r"tpl1646491895337.png", record_pos=(-0.035, 0.297), resolution=(720, 1280))))

touch(wait(Template(r"tpl1646491958576.png", record_pos=(0.018, 0.808), resolution=(720, 1280))))