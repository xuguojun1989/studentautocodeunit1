#coding=utf-8
import sys
sys.path.append("..")
from handle.login.yanzhengmalogin_handle import YanzhengmaloginHandle
from handle.login.userprotocal_handle import UserprotocalHandle
from page.login.userprotocal_page import UserprotocalPage
from page.login.userhideprotocal_page import UserhideprotocalPage
from page.login.login_page import LoginPage
from handle.login.userhideprotocal_handle import UserhideprotocalHandle
from handle.login.login_handle import LoginHandle
import logging


class ProtocalBusiness:
    def __init__(self,driver,createdir):
        self.driver = driver
        self.createdir = createdir
        self.yanzhengmalogin_handle=YanzhengmaloginHandle(self.driver)
        self.login_handle=LoginHandle(self.driver)

    def userprotocal(self):
        logging.info("----用例userprotocal执行开始----")
        dir = self.createdir.createcasedir("userprotocal")
        try:
            logging.info("验证码页面用户协议查看")
            self.yanzhengmalogin_handle.click_userprotocol()
            self.userprotocal_handle = UserprotocalHandle(self.driver)
            self.userprotocal_page=UserprotocalPage(self.driver)
            self.userprotocal_page.get_return_element()
            self.driver.get_screenshot_as_file(dir + '/userprotocal.png')
            self.userprotocal_handle.click_returelogin()
            logging.info("登录页面用户协议查看")
            self.yanzhengmalogin_handle.click_passwordlogin()
            self.login_page= LoginPage(self.driver)
            self.login_page.get_useragrement_element()
            self.login_handle.click_useragrement()
            self.userprotocal_page.get_return_element()
            self.userprotocal_handle.click_returelogin()
            self.login_handle.click_enteryanzhengmalogin()
            self.login_page.get_useragrement_element()
            logging.info("----用例userprotocal执行结束，结果True----")
            return True
        except:
            self.driver.get_screenshot_as_file(dir + '/userprotocal.png')
            logging.info("----用例userprotocal执行结束，结果False----")
            return False

    def userhideprotocal(self):
        try:
            dir = self.createdir.createcasedir("userhideprotocal")
            print("try start")
            logging.info('验证码页面获取用户隐私协议')
            self.yanzhengmalogin_handle.click_userhideprotocol()
            print("验证码页面点击用户隐私协议")
            self.userhideprotocal_page=UserhideprotocalPage(self.driver)
            self.userhideprotocal_page.get_return_element()
            print("查询到用户隐私协议的返回按钮")
            self.driver.get_screenshot_as_file(dir + '/userhideprotocal.png')
            self.userhideprotocal_handle=UserhideprotocalHandle(self.driver)
            self.userhideprotocal_handle.click_returelogin()
            logging.info("验证码页面用户协议查看成功")
            self.yanzhengmalogin_handle.click_passwordlogin()
            self.login_page.get_userhideagrement_element()

            self.login_handle.click_userhideagrement()
            self.userhideprotocal_page.get_return_element()
            self.userhideprotocal_handle.click_returelogin()
            self.login_handle.click_enteryanzhengmalogin()
            self.login_page.get_userhideagrement_element()
            logging.info("----用例userhideprotocal执行结束，结果True----")
            return True

        except:
            self.driver.get_screenshot_as_file(dir + '/userhideprotocal.png')
            logging.info("----用例userhideprotocal执行结束，结果False----")
            return False











