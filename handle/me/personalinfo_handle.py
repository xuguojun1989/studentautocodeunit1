# coding=utf-8
import sys

sys.path.append("..")
from page.me.personalinfo_page import PersonalinfoPage


class PersonalinfoHandle:
    def __init__(self,driver):
        self.personalinfo_page = PersonalinfoPage(driver)

    # 操作个人资料页面的元素
    def click_returelogin(self):
        '''
        点击返回按钮
        '''
        self.personalinfo_page.get_return_element().click()
