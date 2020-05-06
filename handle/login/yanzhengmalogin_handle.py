# coding=utf-8
import sys
sys.path.append("..")
from page.login.yanzhengmalogin_page import Yanzhengmalogin_Page


class YanzhengmaloginHandle:
    def __init__(self,driver):
        self.yanzhengmalogin_page = Yanzhengmalogin_Page(driver)

    # 操作登录页面的元素
    def click_passwordlogin(self):
        '''
        点击密码登录
        '''
        self.yanzhengmalogin_page.get_password_login_element().click()

    def click_userprotocol(self):
        '''
        点击用户协议
        '''
        self.yanzhengmalogin_page.get_user_protocal_element().click()
    def click_userhideprotocol(self):
        '''
        点击用户隐私协议
        '''
        self.yanzhengmalogin_page.get_user_hideprotocal_element().click()
    def click_chlidhideprotocol(self):
        '''
        点击儿童隐私协议
        '''
        self.yanzhengmalogin_page.get_child_hideprotocal_element().click()