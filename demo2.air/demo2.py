# -*- encoding=utf8 -*-
__author__ = "gkxox"

from airtest.core.api import *


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

from airtest.core.api import using
using("public.air")
from public import *

auto_setup(__file__)
for i in range(5):

    poco.scroll("up")
swipe()

poco("ctrip.android.publicproduct:id/flow_recycle_view").swipe([0.0072, 1])
swipe([0.5, 0.8],[0, -0.6],duration=2.0)

for i in range(5):
    poco("ctrip.android.publicproduct:id/hs_product_salelive_cover_iv").swipe([-0.3, 0])

while True:
    
    poco(text='我的').click()
    poco(text='首页').click()

    


