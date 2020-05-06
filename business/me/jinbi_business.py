# coding=utf-8
import sys

sys.path.append("..")
from handle.me.me_handle import MeHandle
from handle.me.jinbi_handle import JinbiHandle
from page.me.jinbi_page import JinbiPage
from handle.index_handle import IndexHandle
from base.login_down import LoginDown
from page.me.me_page import MePage
import logging
from  publicfun.restartapp import RestartApp


class JinbiBusiness:
    def __init__(self, driver, createdir, username):
        self.driver = driver
        self.username = username
        self.createdir = createdir
        self.restart=RestartApp()

    def selcetjinbiinfo(self):
        logging.info('----用例selcetjinbiinfo执行开始----')
        dir = self.createdir.createcasedir("selcetjinbiinfo")
        # logging.info("检查登录状态，如未登录先登录")
        # self.login_down=LoginDown(self.driver)
        # self.login_down.unloginloginfirst()
        try:
            logging.info("从学习页面查看金币动作开始")
            self.index_handle = IndexHandle(self.driver)
            self.index_handle.click_lowerbannerme()
            self.me_handle = MeHandle(self.driver)
            self.me_handle.click_jinbi()
            self.jinbi_handle = JinbiHandle(self.driver)
            self.jinbi_page = JinbiPage(self.driver)
            self.jinbi_page.get_return_element()
            self.driver.get_screenshot_as_file(dir + '/' + self.username + 'selcetpersonalinfo.png')
            self.jinbi_handle.click_returelogin()
            self.me_page=MePage(self.driver)
            self.me_page.get_touxiang_element()
            logging.info("从学习页面查看金币返回我的页面，动作结束")
            logging.info("----用例selcetjinbiinfo执行结果True，执行结束----")
            return True
        except:
            self.driver.get_screenshot_as_file(dir + '/' + self.username + 'selcetpersonalinfo.png')
            #self.driver.startActivity("com.gaosi.student", "com.gaosi.student.ui.loading.SplashingActivity")
            self.restart.restartandroid()
            logging.info("----用例selcetjinbiinfo执行结果False，执行结束----")
            return False









