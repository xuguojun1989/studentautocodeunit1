# coding=utf-8
import sys

sys.path.append("..")
from page.login.protocalalter_page import ProtocalalterPage


class ProtocalalterHandle:
    def __init__(self,driver):
        self.protocalalter_page = ProtocalalterPage(driver)

    # 操作协议弹窗页面的元素
    def click_agreebutton(self):
        '''
        点击同意按钮
        '''
        self.protocalalter_page.get_agree_element().click()

    def click_notagreebutton(self):
        '''
        点击不同意按钮
        '''
        self.protocalalter_page.get_notagree_element().click()