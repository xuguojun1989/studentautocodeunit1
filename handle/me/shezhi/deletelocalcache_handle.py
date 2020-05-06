# coding=utf-8
import sys

sys.path.append("..")
from page.me.shezhi.deletelocalcache_page import DeletelocalcachePage


class DeletelocalcacheHandle:
    def __init__(self,driver):
        self.deletelocalcache_page = DeletelocalcachePage(driver)

    # 操作清除缓存页面的元素
    def click_okbutton(self):
        '''
        点击确定按钮
        '''
        self.deletelocalcache_page.get_ok_element().click()
    def click_cancelbutton(self):
        '''
        点击取消按钮
        '''
        self.deletelocalcache_page.get_cancel_element().click()

