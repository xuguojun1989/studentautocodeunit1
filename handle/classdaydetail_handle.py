# coding=utf-8
import sys

sys.path.append("..")
from page.classdaydetail_page import ClassdaydetailPage

class Classdaydetail_Handle:
    def __init__(self,driver):
        self.classdaydetail_page = ClassdaydetailPage(driver)

    def clickhejiaostudytasks(self):
        '''
        点击禾教口语练习
        '''
        self.classdaydetail_page.get_studytasks_element()[0].click()

    def clickonlinestudytasks(self):
        '''
        点击91提交作业口语练习
        '''
        self.classdaydetail_page.get_studytasks_element()[1].click()

    def clickcoursematerial(self):
        '''
        点击课程资料去查看按钮
        '''
        self.classdaydetail_page.get_studytasks_element()[3].click()

    def click_returnbutton(self):
        '''
        点击课节详情页返回按钮
        '''
        self.classdaydetail_page.get_returnbutton_element().click()

    def clickzhuanticoursetasks(self):
        '''
        点击专题课堂
        '''

        maintext = self.classdaydetail_page.get_studytaskstitle_element()[0].text
        if maintext == "专题课":
            self.classdaydetail_page.get_studytasks_element()[0].click()
        else:
            print("未找到专题课任务")

    def clickselfreinforcementtasks(self):
        '''
        点击自我巩固
        '''
        maintext = self.classdaydetail_page.get_studytaskstitle_element()[1].text
        if maintext == "自我巩固":
            self.classdaydetail_page.get_studytasks_element()[1].click()
        else:
            print("未找到自我巩固任务")




