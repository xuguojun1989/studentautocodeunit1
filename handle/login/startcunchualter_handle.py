# coding=utf-8
import sys

sys.path.append("..")
from page.login.startcunchualter_page import StartcunchualterPage


class StartcunchualterHandle:
    def __init__(self,driver):
        self.startcunchualter_page = StartcunchualterPage(driver)

    # 操作存储弹窗页面的元素
    def click_okbuttonlogin(self):
        '''
        点击确定按钮
        '''
        self.startcunchualter_page.get_okbutton_element().click()
    # 操作系统存储弹窗页面的元素
    def click_sysokbuttonlogin(self):
        '''
        点击允许按钮
        '''
        self.startcunchualter_page.get_sysokbutton_element().click()
