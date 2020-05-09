# coding=utf-8
import sys

sys.path.append("..")

from handle.me.set_handle import SetHandle
from page.me.set_page import SetPage

import logging
from  publicfun.restartapp import RestartApp
from  publicfun.downentersetpage import Downentersetpage
from page.me.shezhi.seteyemode_page import SeteyemodePage
from  page.me.shezhi.seteyemodeconfirm_page import SeteyemodeconfirmPage
from handle.me.shezhi.seteyemode_handle import SeteyemodeHandle
from handle.me.shezhi.seteyemodeconfirm_handle import SeteyemodeconfirmHandle


class SeteyemodeBusiness:
    def __init__(self, driver, createdir, username):
        self.driver = driver
        self.username = username
        self.createdir = createdir
        self.restart=RestartApp()



    def checkfirstset(self):
        self.seteyemode_page=SeteyemodePage(self.driver)
        try:
            self.seteyemode_page.get_ok_element()
            return True
        except:
            return False


    def seteyemode(self):
        dir = self.createdir.createcasedir("seteyemode")
        try:
            logging.info('----用例seteyemode执行开始----')
            # logging.info("检查登录状态，如未登录先登录")
            # self.login_down = LoginDown(self.driver)
            # self.login_down.unloginloginfirst()
            logging.info("检查是否在设置页面，如不在，重新设置页面")
            self.downentersetpage = Downentersetpage(self.driver)
            self.downentersetpage.downentersetpage()
            self.set_handle = SetHandle(self.driver)
            self.set_page=SetPage(self.driver)
            self.set_page.get_protecteye_element()
            self.set_handle.click_eyemode()
            #self.driver.switch_to.alert.accept()
            print(self.checkfirstset())
            if self.checkfirstset():
                self.seteyemode_handle=SeteyemodeHandle(self.driver)
                self.seteyemode_handle.click_okbutton()

                self.seteyemodeconfirm_page=SeteyemodeconfirmPage(self.driver)
                self.seteyemodeconfirm_page.get_set_element()
                self.seteyemodeconfirm_handle=SeteyemodeconfirmHandle(self.driver)
                self.seteyemodeconfirm_handle.click_setbutton(self.driver)
                self.driver.keyevent(4)
                self.set_page.get_protecteye_element()
                return True
            else:
                self.set_page.get_protecteye_element()
                self.driver.get_screenshot_as_file(dir + '/'+self.username+'seteyemode.png')
                logging.info('----用例seteyemode执行结果True，执行结束----')
                return True
        except:
            self.driver.get_screenshot_as_file(dir + '/'+self.username+'seteyemode.png')
            self.restart.restartandroid()
            logging.info('----用例seteyemode执行结果Flase，执行结束----')
            return False




