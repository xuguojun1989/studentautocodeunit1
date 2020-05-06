# coding=utf-8
import sys

sys.path.append("..")
from page.shengji_page import ShengjiPage

class ShengjiHandle:
    def __init__(self,driver):
        self.shengji_page = ShengjiPage(driver)


    def click_update(self):
        '''
        点击立即更新按钮
        '''
        self.shengji_page.get_update_element().click()

    def click_cancel(self):
        '''
        点击取消按钮
        '''
        self.shengji_page.get_cancel_element().click()