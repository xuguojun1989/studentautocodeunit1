# coding=utf-8
import sys

sys.path.append("..")
from page.login.userhideprotocal_page import UserhideprotocalPage


class UserhideprotocalHandle:
    def __init__(self,driver):
        self.userhideprotocal_page = UserhideprotocalPage(driver)

    # 操作用户隐私协议页面的元素
    def click_returelogin(self):
        '''
        点击返回按钮
        '''
        self.userhideprotocal_page.get_return_element().click()
