# coding=utf-8
import sys

sys.path.append("..")
from page.correctresult_page import CorrectresultPage

class CorrectresultHandle:
    def __init__(self,driver):
        self.correctresult_page = CorrectresultPage(driver)


    def click_returnbutton(self):
        '''
        点击批改结果返回按钮
        '''
        self.correctresult_page.get_returnbutton_element().click()