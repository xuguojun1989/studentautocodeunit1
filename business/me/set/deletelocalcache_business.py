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


class DeletelocalcacheBusiness:
    def __init__(self, driver, createdir, username):
        self.driver = driver
        self.username = username
        self.createdir = createdir
        self.restart=RestartApp()



    def deletelocalcache(self):
        dir = self.createdir.createcasedir("deletelocalcache")
        try:
            logging.info('----用例deletelocalcache执行开始----')
            # logging.info("检查登录状态，如未登录先登录")
            # self.login_down = LoginDown(self.driver)
            # self.login_down.unloginloginfirst()
            logging.info("检查是否在设置页面，如不在，重新设置页面")
            self.downentersetpage = Downentersetpage(self.driver)
            self.downentersetpage.downentersetpage()
            self.set_handle = SetHandle(self.driver)
            self.set_page=SetPage(self.driver)
            if self.set_page.get_deletecache_element().text == "0K":
                logging.info("检查当前没有缓存数据")
                self.set_handle.click_deletecache()
                self.set_page.get_toast_element('当前没有缓存哦')
                self.driver.get_screenshot_as_file(dir + '/' + self.username + 'deletelocalcache.png')
                logging.info("----用例deletelocalcache执行结果True，执行结束----")
                return True
            else:
                self.set_handle.click_deletecache()
                self.deletelocalcache_handle=DeletelocalcacheHandle(self.driver)
                self.deletelocalcache_page=DeletelocalcachePage(self.driver)
                self.deletelocalcache_page.get_ok_element()
                self.deletelocalcache_handle.click_okbutton()
                self.set_page.get_toast_element('清理成功')
                self.set_page.get_deletecache_element()
                self.driver.get_screenshot_as_file(dir + '/' + self.username + 'deletelocalcache.png')
                logging.info("检测到有缓存数据并清除成功，动作结束")
                logging.info("----用例deletelocalcache执行结果True，执行结束----")
                return True
        except:
            self.driver.get_screenshot_as_file(dir + '/' + self.username + 'deletelocalcache.png')
            #self.driver.startActivity("com.gaosi.student", "com.gaosi.student.ui.loading.SplashingActivity")
            self.restart.restartandroid()
            logging.info("----用例deletelocalcache执行结果False，执行结束----")
            return False
