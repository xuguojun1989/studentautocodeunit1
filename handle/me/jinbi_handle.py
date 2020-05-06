# coding=utf-8
import sys

sys.path.append("..")
from page.me.jinbi_page import JinbiPage


class JinbiHandle:
    def __init__(self,driver):
        self.jinbi_page = JinbiPage(driver)

    # 操作用户隐私协议页面的元素
    def click_returelogin(self):
        '''
        点击返回按钮
        '''
        self.jinbi_page.get_return_element().click()
