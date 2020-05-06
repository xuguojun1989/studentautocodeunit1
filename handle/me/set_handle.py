# coding=utf-8
import sys

sys.path.append("..")
from page.me.set_page import SetPage


class SetHandle:
    def __init__(self,driver):
        self.set_page = SetPage(driver)

    # 操作设置页面的元素
    def click_cancellogin(self):
        '''
        点击退出登录
        '''
        print(self.set_page.get_cancellogin_element())
        self.set_page.get_cancellogin_element().click()

    def click_cancelusername(self):
        '''
        点击注销账号登录
        '''
        self.set_page.get_cancelusername_element().click()

    def click_deletecache(self):
        '''
        点击清除缓存按钮
        '''
        self.set_page.get_deletecache_element().click()

    def click_checknewversion(self):
        '''
        点击检查最新版本按钮
        '''
        self.set_page.get_checkversion_element()

