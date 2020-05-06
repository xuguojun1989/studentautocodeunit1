# coding=utf-8
import sys

sys.path.append("..")
from page.index_page import IndexPage


class IndexHandle:
    def __init__(self,driver):
        self.index_page = IndexPage(driver)

    # 操作底栏我的元素
    def click_lowerbannerme(self):
        '''
        点击低栏我的
        '''
        self.index_page.get_lowbannerme_element().click()

    def click_coursereadstatus(self):
        '''
        点击在读状态
        '''
        self.index_page.get_coursereadstatus_element().click()
    def click_coursesubject(self):
        '''
        点击科目选项
        '''
        self.index_page.get_coursesubject_element().click()
    def click_coursereadstatus(self):
        '''
        点击在读状态选择框
        '''
        self.index_page.get_coursereadstatus_element().click()
    def click_coursesubject(self):
        '''
        点击科目选择框
        '''
        self.index_page.get_coursesubject_element().click()

    def click_jiekestatus(self):
        '''
        选择已结课
        '''
        self.index_page.get_jiekestatus_element().click()

    def click_subject(self):
        '''
        选择语文科目
        '''
        self.index_page.get_subject_element()[2].click()

    def click_course(self):
        '''
        点击课程1
        '''
        self.index_page.get_course_element()[0].click()

    def click_course1(self):
        '''
        点击课程3
        '''
        self.index_page.get_course1_element()[2].click()

