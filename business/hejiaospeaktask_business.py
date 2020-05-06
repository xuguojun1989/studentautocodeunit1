#coding=utf-8
import sys
sys.path.append("..")
from page.classdaydetail_page import ClassdaydetailPage
from  time import  sleep

class ClassdaydetailplaybackBusiness:
    def __init__(self,driver):
        self.driver = driver

    #检查禾教口语练习功能,禾教课返回按钮可以找到，可以优化
    def checkhejiaotask(self):

        self.classdaydetail_page= ClassdaydetailPage(self.driver)
        sleep(2)
        self.classdaydetail_page.get_playbackstatus_element().click()