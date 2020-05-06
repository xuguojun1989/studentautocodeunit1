# coding=utf-8
import sys

sys.path.append("..")
from page.agreeornot_page import AgreeornotPage



class MeHandle:
    def __init__(self,driver):
        self.agreeornot_page = AgreeornotPage(driver)


    def click_set(self):
        '''
        点击专题课弹窗坚持退出按钮按钮
        '''
        self.agreeornot_page.get_set_element()[0].click()