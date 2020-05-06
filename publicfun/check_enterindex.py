#coding=utf-8
from page.index_page import IndexPage
from page.shengji_page import ShengjiPage
from handle.shengji_handle import ShengjiHandle
class CheckenterIndex:
    def __init__(self,driver):
        self.driver=driver

#检查是否登录成功
    def checkindex(self):
        self.index_page=IndexPage(self.driver)
        try:
            self.index_page.get_lowbannerstudy_element()
            return True
        except:
            return False
    def checkshengji(self):
        self.shengji_page=ShengjiPage(self.driver)
        try:
            self.shengji_page.get_update_element()
            return True
        except:
            return False
    def checkenterindex(self):
        if self.checkindex() is True:
            return True
        elif self.checkshengji() is True:
            self.shengji_handle=ShengjiHandle(self.driver)
            self.shengji_handle.click_cancel()
            return True
        else:
            return  False
