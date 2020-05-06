# coding=utf-8
import sys

sys.path.append("..")
from page.me.shezhi.surelogout_page import SurelogoutPage


class SurelogoutHandle:
    def __init__(self,driver):
        self.surelogout_page = SurelogoutPage(driver)

    # 操作设置页面的元素
    def click_oklogoutlogin(self):
        '''
        点击确定退出按钮
        '''
        self.surelogout_page.get_oklogoutlogin_element().click()

    def click_cancellogoutlogin(self):
        '''
        点击取消退出按钮
        '''
        self.surelogout_page.get_cancellogoutlogin_element().click()
