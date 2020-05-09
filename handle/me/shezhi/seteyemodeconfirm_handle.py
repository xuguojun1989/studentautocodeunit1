# coding=utf-8
import sys

sys.path.append("..")
from page.me.shezhi.seteyemodeconfirm_page import SeteyemodeconfirmPage


class SeteyemodeconfirmHandle:
    def __init__(self,driver):
        self.seteyemodeconfirm_page = SeteyemodeconfirmPage(driver)

    # 操作护眼模式弹窗设置页面
    def click_setbutton(self):
        '''
        点击设置按钮
        '''
        self.seteyemodeconfirm_page.get_set_element().click()


