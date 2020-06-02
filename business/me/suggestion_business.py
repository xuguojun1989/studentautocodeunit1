# coding=utf-8
import sys

sys.path.append("..")

from handle.me.me_handle import MeHandle
from page.me.me_page import MePage
import logging
from  publicfun.restartapp import RestartApp
from page.me.shezhi.suggestion_page import SuggestionPage
from handle.me.suggestion_handle import SuggestionHandle
from handle.index_handle import IndexHandle


class SuggestionBusiness:
    def __init__(self, driver, createdir, username):
        self.driver = driver
        self.username = username
        self.createdir = createdir
        self.restart=RestartApp()

    def submitsuggestion(self):
        dir = self.createdir.createcasedir("submitsuggestion")
        logging.info('----用例submitsuggestion执行开始----')
        try:
            self.index_handle = IndexHandle(self.driver)
            self.index_handle.click_lowerbannerme()
            self.me_handle = MeHandle(self.driver)
            self.me_page=MePage(self.driver)
            # self.me_page.get_suggestion_element()
            self.me_handle.click_suggestion()
            self.suggestion_page=SuggestionPage(self.driver)
            self.suggestion_page.get_return_element()
            self.suggestion_handle=SuggestionHandle(self.driver)
            self.suggestion_handle.send_suggestion("这里是意见反馈内容，高思内部员工测试~")
            self.suggestion_handle.click_submitbutton()
            self.driver.get_screenshot_as_file(dir + '/'+self.username+'submitsuggestion.png')
            self.suggestion_page.get_editsuggestion_element()
            #self.suggestion_page.get_toast_element("提交成功")
            self.me_page.get_touxiang_element()
            logging.info('----用例submitsuggestion执行结果True，执行结束----')
            return True
        except:
            self.driver.get_screenshot_as_file(dir + '/' + self.username + 'submitsuggestion.png')
            self.restart.restartandroid()
            logging.info("----用例submitsuggestion执行结果False，执行结束----")
            return False




