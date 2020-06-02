# coding=utf-8
import sys

sys.path.append("..")
from handle.me.set_handle import SetHandle
from page.me.set_page import SetPage
from page.me.shezhi.withus_page import WithusPage
from handle.me.shezhi.withuspagehandle import WithusHandle
import logging
from  publicfun.restartapp import RestartApp
from  publicfun.downentersetpage import Downentersetpage



class WithusBusiness:
    def __init__(self, driver, createdir, username):
        self.driver = driver
        self.username = username
        self.createdir = createdir
        self.restart=RestartApp()

    def checkwithuspage(self):
        dir = self.createdir.createcasedir("checkwithuspage")
        try:
            logging.info('----用例checkwithuspage执行开始----')
            # logging.info("检查登录状态，如未登录先登录")
            # self.login_down = LoginDown(self.driver)
            # self.login_down.unloginloginfirst()
            self.downentersetpage = Downentersetpage(self.driver)
            self.downentersetpage.downentersetpage()
            self.set_handle = SetHandle(self.driver)
            self.set_handle.click_withus()
            self.withus_page=WithusPage(self.driver)
            self.withus_page.get_userprotocal_element()
            self.withus_handle=WithusHandle(self.driver)
            self.withus_handle.click_returnbutton()
            self.set_page=SetPage(self.driver)
            self.set_page.get_return_element()
            self.set_handle.click_returnbutton()
            logging.info("查看关于我们页面，动作结束")
            logging.info("----用例checkwithuspage执行结果True，执行结束----")
            return True
        except:
            self.driver.get_screenshot_as_file(dir + '/' + self.username + 'checkwithuspage.png')
            #self.driver.startActivity("com.gaosi.student", "com.gaosi.student.ui.loading.SplashingActivity")
            self.restart.restartandroid()
            logging.info("----用例checkzhuxiaouserpage执行结果False，执行结束----")
            return False



