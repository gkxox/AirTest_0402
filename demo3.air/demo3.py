# -*- encoding=utf8 -*-
__author__ = "gkxox"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# from airtest.core.api import using
# using("public.air")
# from public import *

poco('android:id/search_src_text').set_text('isrptest14')