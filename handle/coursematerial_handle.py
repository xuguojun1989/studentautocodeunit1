# coding=utf-8
import sys

sys.path.append("..")
from page.coursematerial_page import CoursematerialPage

class CoursematerialHandle:
    def __init__(self,driver):
        self.coursematerial_page = CoursematerialPage(driver)


    def click_returnbutton(self):
        '''
        点击课程资料返回按钮
        '''
        self.coursematerial_page.get_returnbutton_element().click()

    def click_pdfmaterial(self):
        '''
        点击课程资料pdf资料
        '''
        self.coursematerial_page.get_pdfmaterial_element()[2].click()

    #已结课语文筛选第一个课程
    def click_classjiangyipdfmaterial(self):
        '''
        点击课堂讲义pdf资料
        '''
        self.coursematerial_page.get_pdfmaterial_element()[0].click()

    #已结课语文筛选第一个课程
    def click_pdfmaterial(self):
        '''
        点击课堂补充pdf资料
        '''
        self.coursematerial_page.get_pdfmaterial_element()[1].click()