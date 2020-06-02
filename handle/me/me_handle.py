# coding=utf-8
import sys

sys.path.append("..")
from page.me.me_page import MePage



class MeHandle:
    def __init__(self,driver):
        self.me_page = MePage(driver)


    def click_set(self):
        '''
        点击我的页面设置按钮
        '''

        print("classname num 4 text is" +self.me_page.get_set_element()[4].text)
        num = len(self.me_page.get_set_element())
        x = 0
        while x<num:
            if self.me_page.get_set_element()[x].text == "设置":
                self.me_page.get_set_element()[x].click()
                break
            x = x + 1

    def click_touxiang(self):
        '''
        点击我的页面头像按钮
        '''
        self.me_page.get_touxiang_element().click()
    def click_jinbi(self):
        '''
        点击我的页面金币按钮
        '''
        self.me_page.get_jinbi_element().click()


    def click_suggestion(self):
        '''
        点击我的页面意见反馈按钮
        '''

        num = len(self.me_page.get_set_element())
        x = 0
        while x<num:
            if self.me_page.get_set_element()[x].text == "意见反馈":
                self.me_page.get_set_element()[x].click()
                break
            x = x + 1

