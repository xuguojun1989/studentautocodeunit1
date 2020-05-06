#coding=utf-8
import sys
sys.path.append("..")
from handle.login.login_handle import LoginHandle
from page.login.yanzhengmalogin_page import Yanzhengmalogin_Page
from handle.login.yanzhengmalogin_handle import  YanzhengmaloginHandle
from  publicfun.get_userinfopublic import Getuserinfopublic
from page.login.login_page import LoginPage


class LoginDown:
    def __init__(self,driver):
        self.driver=driver
        self.get_userinfopublic=Getuserinfopublic()
        self.username=self.get_userinfopublic.getusername()
        self.pwd=self.get_userinfopublic.getpwd()


    def checkloginstatus(self):
        try:
            self.yanzhengmalogin_page = Yanzhengmalogin_Page(self.driver)
            self.yanzhengmalogin_page.get_password_login_element()
            return False
        except:
            return  True

    def unloginloginfirst(self):

        flag = self.checkloginstatus()
        if flag is False:
            self.yanzhengmalogin_handle = YanzhengmaloginHandle(self.driver)
            self.yanzhengmalogin_handle.click_passwordlogin()

            self.login_handle = LoginHandle(self.driver)
            self.login_page=LoginPage(self.driver)
            self.login_page.get_username_element()
            self.login_handle.send_username(self.username)
            self.login_handle.send_password(self.pwd)
            self.login_handle.click_login()



