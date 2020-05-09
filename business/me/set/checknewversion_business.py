# coding=utf-8
import sys

sys.path.append("..")

from handle.me.set_handle import SetHandle
from page.me.set_page import SetPage
from handle.me.shezhi.deletelocalcache_handle import DeletelocalcacheHandle
from base.login_down import LoginDown
import logging
from  publicfun.restartapp import RestartApp
from  publicfun.downentersetpage import Downentersetpage
from page.me.shezhi.deletelocalcache_page import DeletelocalcachePage


class ChecknewversionBusiness:
    def __init__(self, driver, createdir, username):
        self.driver = driver
        self.username = username
        self.createdir = createdir
        self.restart=RestartApp()



    def deletelocalcache(self):
        dir = self.createdir.createcasedir("deletelocalcache")

        logging.info('----用例checknewversion执行开始----')
        # logging.info("检查登录状态，如未登录先登录")
        # self.login_down = LoginDown(self.driver)
        # self.login_down.unloginloginfirst()
        logging.info("检查是否在设置页面，如不在，重新设置页面")
        self.downentersetpage = Downentersetpage(self.driver)
        self.downentersetpage.downentersetpage()
        self.set_handle = SetHandle(self.driver)
        self.set_page=SetPage(self.driver)
