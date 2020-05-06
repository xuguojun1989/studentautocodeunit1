#coding=utf-8
import sys
sys.path.append("..")
from page.login.login_page import LoginPage

class LoginHandle:
    def __init__(self,driver):
        self.login_page = LoginPage(driver)

    #操作登录页面的元素
    def click_passwordlogin(self):
        '''
        点击密码登录
        '''
        self.login_page.get_password_login_element().click()

    def send_username(self,user):
        '''
        输入用户名
        '''
        self.login_page.get_username_element().send_keys(user)

    def send_password(self,password):
        '''
        输入密码
        '''
        self.login_page.get_password_element().send_keys(password)

    def click_login(self):
        '''
        点击登录按钮
        '''
        self.login_page.get_login_button_element().click()

    def click_enteryanzhengmalogin(self):
        '''
        点击验证码登录
        '''
        self.login_page.get_enteryanzhengmalogin_element().click()

    def click_useragrement(self):
        '''
        点击获取用户协议
        '''
        self.login_page.get_useragrement_element().click()

    def click_userhideagrement(self):
        '''
        点击获取用户隐私协议
        '''
        self.login_page.get_userhideagrement_element().click()

