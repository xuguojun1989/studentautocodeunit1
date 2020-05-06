#coding=utf-8
import sys
sys.path.append("..")
from page.index_page import IndexPage
from time import sleep
from handle.index_handle import IndexHandle
from base.login_down import LoginDown
from base.swipe import Swipe

class CourseBusiness:
    def __init__(self,driver):
        self.driver=driver


    #选择已结课语文查询,检查查询是否正确
    def jiekeyuwenselect(self):
        sleep(2)
        self.login_down =LoginDown(self.driver)
        self.login_down.unloginloginfirst()
        sleep(3)
        print('执行滑动屏幕开始')
        self.swipe=Swipe(self.driver)
        self.swipe.swipe_up()
        print('执行滑动屏幕结束')
        sleep(1)
        self.index_handle=IndexHandle(self.driver)
        self.index_handle.click_coursereadstatus()
        sleep(1)
        self.index_handle.click_jiekestatus()
        sleep(1)
        self.index_handle.click_coursesubject()
        sleep(1)
        self.index_handle.click_subject()
        sleep(1)
        self.index_page = IndexPage(self.driver)
        try:
            self.index_page.get_course_element()
            return True
        except:
            return False