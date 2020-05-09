# coding=utf-8
import sys

sys.path.append("..")
from page.me.shezhi.seteyemode_page import SeteyemodePage


class SeteyemodeHandle:
    def __init__(self,driver):
        self.seteyemode_page = SeteyemodePage(driver)

    # 操作护眼模式弹窗
    def click_okbutton(self):
        '''
        点击确定按钮
        '''
        self.seteyemode_page.get_ok_element().click()
    def click_cancelbutton(self):
        '''
        点击取消按钮
        '''
        self.seteyemode_page.get_cancel_element().click()

