# coding=utf-8
import sys

sys.path.append("..")
from page.login.userprotocal_page import UserprotocalPage


class UserprotocalHandle:
    def __init__(self,driver):
        self.userprotocal_page = UserprotocalPage(driver)

    # 操作用户协议页面的元素
    def click_returelogin(self):
        '''
        点击返回按钮
        '''
        self.userprotocal_page.get_return_element().click()
