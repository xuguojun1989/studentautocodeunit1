# coding=utf-8
import sys

sys.path.append("..")
from page.zhuxiaouser_page import ZhuxiaouserPage


class ZhuxiaouserHandle:
    def __init__(self,driver):
        self.zhuxiaouser_page = ZhuxiaouserPage(driver)

    # 操作注销账号页面的元素
    def click_returelogin(self):
        '''
        点击返回按钮
        '''
        self.zhuxiaouser_page.get_return_element().click()
