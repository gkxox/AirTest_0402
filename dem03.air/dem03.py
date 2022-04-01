# -*- encoding=utf8 -*-
__author__ = "gkxox"

from airtest.core.api import *


auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

wake()

dev = device()
dev.pinch(center=None, percent=0.5, duration=0.5, steps=5, in_or_out='out')
dev.pinch(center=None, percent=0.5, duration=0.5, steps=5, in_or_out='in')
sleep(1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
home()
sleep(1)
dev.two_finger_swipe((627,1833),(627,474))


poco('com.tencent.mm:id/dtj').click()
