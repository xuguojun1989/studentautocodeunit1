# coding=utf-8
import sys

sys.path.append("..")
from page.zhuanticourse_page import ZhuantiCoursePage

class ZhuanticourseHandle:
    def __init__(self,driver):
        self.zhuanticourse_page = ZhuantiCoursePage(driver)

    def click_returnbutton(self):
        '''
        点击专题课返回按钮
        '''
        self.zhuanticourse_page.get_zhuanticoursereturn_element().click()

    def click_subjectchooseA(self):
        '''
        点击专题课题目选项A按钮
        '''
        self.zhuanticourse_page.get_zhuanticoursesubjectchoose_elements()[0].click()