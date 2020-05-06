#coding=utf-8
import sys
sys.path.append("..")
from handle.protocalalter_handle import ProtocalalterHandle
from page.login.protocalalter_page import ProtocalalterPage
from page.login.yanzhengmalogin_page import Yanzhengmalogin_Page
import logging

class ProtocalalterBusiness():
    def __init__(self,driver,createdir):
        self.driver=driver
        self.createdir=createdir

    def checkagreebuttonexist(self):
        try:
            self.protocalalter_page=ProtocalalterPage(self.driver)
            self.protocalalter_page.get_agree_element()
            return True
        except:
            return False

    def clickagreebutton(self):
        logging.info("----用例clickagreebutton执行开始-----")
        dir = self.createdir.createcasedir("clickagreebutton")
        if self.checkagreebuttonexist() is True:
            logging.info("检查到协议弹窗")
            self.protocalalter_handle=ProtocalalterHandle(self.driver)
            self.protocalalter_handle.click_agreebutton()
            self.driver.switch_to.alert.accept()
            self.yanzhengmalogin_page=Yanzhengmalogin_Page(self.driver)
            self.yanzhengmalogin_page.get_password_login_element()
            self.driver.get_screenshot_as_file(dir + '/clickagreebutton.png')
            logging.info("----用例clickagreebutton执行结果True，执行结束----")
            return True
        else:
            logging.info('未检查到协议弹窗')
            self.driver.get_screenshot_as_file(dir + '/clickagreebutton.png')
            logging.info("----用例clickagreebutton执行结果False，执行结束----")
            return False






