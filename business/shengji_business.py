#coding=utf-8
import sys
sys.path.append("..")
from time import sleep
from handle.index_handle import IndexHandle
from page.classdaylist_page import ClassdaylistPage
from page.shengji_page import ShengjiPage

class ShengjiBusiness:
    def __init__(self,driver):
        self.driver=driver

    def clickupdate(self):
        try:
            self.shengji_page = ShengjiPage(self.driver)
            sleep(3)
            self.shengji_page.get_update_element()
            print('查询到课程')
            return True
        except:
            print('未查询到课程')
            return False

    def classdetailselect(self):
        if self.getcourseelement():
            self.index_handle = IndexHandle(self.driver)
            self.index_handle.click_course()
            print('执行完成点击课程')
            sleep(2)
            self.classdaylist_page = ClassdaylistPage(self.driver)
            elements = self.classdaylist_page.get_classdayviewgroup_elements()
            classdaystatus = self.classdaylist_page.get_coursedaystatus_elements()[0].text
            #if len(elements) == 11 and classdaystatus ==  "已下课":
            if len(elements) == 10 and classdaystatus ==  "已下课":
                return True
        else:
            return  False