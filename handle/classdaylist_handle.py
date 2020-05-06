# coding=utf-8
import sys

sys.path.append("..")
from page.classdaylist_page import ClassdaylistPage


class Classdaylist_Handle:
    def __init__(self,driver):
        self.classdaylist_page = ClassdaylistPage(driver)

    def click_classdaylist(self):
        '''
        点击该课程下第一讲
        '''
        self.classdaylist_page.get_coursedaystatus_elements()[0].click()

    def click_classdaylist3(self):
        '''
        点击该课程下第三讲
        '''
        self.classdaylist_page.get_coursedaystatus_elements()[2].click()

    def click_returnbutton(self):
        '''
        点击课程详情页返回按钮
        '''
        self.classdaylist_page.get_returnbutton_element().click()

