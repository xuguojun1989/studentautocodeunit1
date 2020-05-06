# coding=utf-8
import sys

sys.path.append("..")
from handle.me.me_handle import MeHandle
from handle.me.personalinfo_handle import PersonalinfoHandle
from page.me.personalinfo_page import PersonalinfoPage
from handle.index_handle import IndexHandle
from base.login_down import LoginDown
import logging
from  publicfun.restartapp import RestartApp


class PersonalinfoBusiness:
    def __init__(self, driver, createdir, username):
        self.driver = driver
        self.username = username
        self.createdir = createdir
        self.restart=RestartApp()

    def selcetpersonalinfo(self):
        logging.info('----用例selcetpersonalinfo执行开始----')
        dir = self.createdir.createcasedir("selcetpersonalinfo")
        logging.info("检查登录状态，如未登录先登录")
        self.login_down=LoginDown(self.driver)
        self.login_down.unloginloginfirst()
        try:
            logging.info("从学习页面查看个人资料动作开始")
            self.index_handle = IndexHandle(self.driver)
            self.index_handle.click_lowerbannerme()
            self.me_handle = MeHandle(self.driver)
            self.me_handle.click_touxiang()
            self.personalinfo_handle = PersonalinfoHandle(self.driver)
            self.personalinfo_page = PersonalinfoPage(self.driver)
            self.personalinfo_page.get_name_element()
            self.driver.get_screenshot_as_file(dir + '/' + self.username + 'selcetpersonalinfo.png')
            self.personalinfo_handle.click_returelogin()
            logging.info("从学习页面查看个人资料返回我的页面，动作结束")
            logging.info("----用例selcetpersonalinfo执行结果True，执行结束----")
            return True
        except:
            self.driver.get_screenshot_as_file(dir + '/' + self.username + 'selcetpersonalinfo.png')
            #self.driver.startActivity("com.gaosi.student", "com.gaosi.student.ui.loading.SplashingActivity")
            self.restart.restartandroid()
            logging.info("----用例selcetpersonalinfo执行结果False，执行结束----")
            return False









