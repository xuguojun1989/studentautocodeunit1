#coding=utf-8
from handle.index_handle import IndexHandle
from handle.me.me_handle import MeHandle
from page.me.set_page import SetPage


class Downentersetpage:
    def __init__(self,driver):
        self.driver=driver

    #检查是否在set页面
    def checksetpage(self):
        try:
            self.set_page=SetPage(self.driver)
            self.set_page.get_deletecache_element()
            return True
        except:
            return False
    #如果不在set页面，进入set页面
    def downentersetpage(self):
        if self.checksetpage() is False:
                self.index_handle=IndexHandle(self.driver)
                self.index_handle.click_lowerbannerme()
                self.me_handle=MeHandle(self.driver)
                self.me_handle.click_set()



