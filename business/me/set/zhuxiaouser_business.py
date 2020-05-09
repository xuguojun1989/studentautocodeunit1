# coding=utf-8
import sys

sys.path.append("..")
from handle.me.set_handle import SetHandle
from page.me.shezhi.zhuxiaouser_page import ZhuxiaouserPage
from handle.me.shezhi.zhuxiao_handle import ZhuxiaouserHandle
from page.me.set_page import SetPage
from base.login_down import LoginDown
import logging
from  publicfun.restartapp import RestartApp
from  publicfun.downentersetpage import Downentersetpage
from handle.index_handle import IndexHandle
from handle.me.me_handle import MeHandle
from page.me.me_page import MePage


class ZhuxiaouserBusiness:
    def __init__(self, driver, createdir, username):
        self.driver = driver
        self.username = username
        self.createdir = createdir
        self.restart=RestartApp()

    def checkzhuxiaouserpage(self):
        dir = self.createdir.createcasedir("checkzhuxiaouserpage")
        try:
            logging.info('----用例checkzhuxiaouserpage执行开始----')
            # logging.info("检查登录状态，如未登录先登录")
            # self.login_down = LoginDown(self.driver)
            # self.login_down.unloginloginfirst()
            logging.info("从学习页面查看注销账号动作开始")
            self.index_handle = IndexHandle(self.driver)
            self.index_handle.click_lowerbannerme()
            self.me_page=MePage(self.driver)
            self.me_page.get_set_element()
            self.me_handle=MeHandle(self.driver)
            self.me_handle.click_set()
            self.set_handle = SetHandle(self.driver)
            self.set_page=SetPage(self.driver)
            print("开始设置页面元素")
            if self.set_page.get_cancellogin_element().text == "退出登录":
                print("页面进入设置页面")
            else:
                print("页面未进入设置页面")
            print("开始点击注销账号按钮")
            #self.set_handle.click_cancelusername()
            self.set_handle.click_cancelusernametext()
            print("点击结束注销账号按钮")
            self.zhuxiaouser_page = ZhuxiaouserPage(self.driver)
            print("检查注销账号页面标题是否存在")
            if self.zhuxiaouser_page.get_title_element().text == "账号注销":
                print("进入账号注销页")
            else:
                print("未进入账号注销页")
            self.driver.get_screenshot_as_file(dir + '/' + self.username + 'checkzhuxiaouserpage.png')
            self.zhuxiao_handle=ZhuxiaouserHandle(self.driver)
            print("点击注销账号页面返回")
            self.zhuxiao_handle.click_returnbutton()
            print("点击注销账号页面返回按钮成功")
            self.set_page.get_cancelusername_element()
            logging.info("查看注销页面页面，动作结束")
            logging.info("----用例checkzhuxiaouserpage执行结果True，执行结束----")
            return True
        except:
            self.driver.get_screenshot_as_file(dir + '/' + self.username + 'checkzhuxiaouserpage.png')
            #self.driver.startActivity("com.gaosi.student", "com.gaosi.student.ui.loading.SplashingActivity")
            self.restart.restartandroid()
            logging.info("----用例checkzhuxiaouserpage执行结果False，执行结束----")
            return False



