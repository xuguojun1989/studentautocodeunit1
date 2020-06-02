# coding=utf-8
import sys

sys.path.append("..")
from page.me.shezhi.withus_page import WithusPage


class WithusHandle:
    def __init__(self,driver):
        self.withus_page = WithusPage(driver)

    # 操作关于我们弹窗设置页面
    def click_returnbutton(self):
        '''
        点击返回按钮
        '''
        self.withus_page.get_return_element().click()

    def click_userprotocalbutton(self):
        '''
        点击用户协议按钮
        '''
        self.withus_page.get_userprotocal_element().click()


