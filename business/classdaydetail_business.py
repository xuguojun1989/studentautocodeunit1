#coding=utf-8
import sys
sys.path.append("..")
from handle.classdaylist_handle import Classdaylist_Handle
from page.classdaydetail_page import ClassdaydetailPage
from  time import  sleep

from handle.classdaydetail_handle import Classdaydetail_Handle
from page.correctresult_page import CorrectresultPage
from handle.correctresult_handle import CorrectresultHandle
from base.swipe import Swipe
from handle.coursematerial_handle import CoursematerialHandle
from page.pdfpreview_page import PdfpreviewPage
from handle.pdfpreview_handle import PdfpreviewHandle
from handle.index_handle import IndexHandle
from  handle.zhuanticourse_handle import ZhuanticourseHandle
from appium.webdriver.common.touch_action import TouchAction
from page.zhuanticourse_page import ZhuantiCoursePage
from page.selfreinforcement_page import SelfreinforcementPage
from handle.selfreinforcement_handle import SelfreinforcementHandle

class ClassdaydetailBusiness:
    def __init__(self,driver):
        self.driver = driver
        self.classdaydetail_handle = Classdaydetail_Handle(self.driver)
        self.classdaydetail_page= ClassdaydetailPage(self.driver)
        self.coursematerial_handle=CoursematerialHandle(self.driver)
        self.classdaylist_handle = Classdaylist_Handle(self.driver)
        self.index_handle=IndexHandle(self.driver)




    # 检查直播状态
    def checklivestatus(self):
        self.classdaylist_handle.click_classdaylist()
        sleep(2)
        try:
            self.classdaydetail_page.get_playbackstatus_element()
            return True
        except:
            return False

    #检查禾教元素展示
    def checkhejiaoshow(self):
        sleep(1)
        hejiaomain = self.classdaydetail_page.get_studytasks_element()[0].text
        hejiaomaintitle=self.classdaydetail_page.get_studytaskstitle_element()[0].text
        print("禾教入口"+hejiaomain)
        print("禾教标题" + hejiaomaintitle)
        if hejiaomain == "去练习" and hejiaomaintitle == "英语口语":
            return True
        else:
            return False


    # 点击第一个自我巩固任务，检查老师评语是否正确
    def checkteacherremark(self):
        self.classdaydetail_handle.clickonlinestudytasks()
        sleep(2)
        self.correctresult_page= CorrectresultPage(self.driver)
        teacherremark=self.correctresult_page.get_teacherremark_element().text
        if teacherremark == "很好":
            return True
        else:
            return False

    #返回课节详情页，点击课程资料，检查内容
    def checklivematerial(self):
        self.correctresult_handle=CorrectresultHandle(self.driver)
        self.correctresult_handle.click_returnbutton()
        sleep(2)
        self.swipe = Swipe(self.driver)
        self.swipe.swipe_up()
        sleep(2)
        self.classdaydetail_handle.clickcoursematerial()
        sleep(2)
        self.coursematerial_handle.click_pdfmaterial()
        sleep(8)
        self.pdfpreview_page=PdfpreviewPage(self.driver)
        try:
            self.pdfpreview_page.get_pdfpreview_element()
            return True
        except:
            return False

    #从预览pdf页面逐步返回到首页
    def returnindex(self):
        self.pdfpreview_handle=PdfpreviewHandle(self.driver)
        sleep(2)
        self.pdfpreview_handle.click_returnbutton()
        sleep(3)
        self.coursematerial_handle.click_returnbutton()
        sleep(3)
        self.classdaydetail_handle.click_returnbutton()
        sleep(3)
        self.classdaylist_handle.click_returnbutton()
        sleep(3)



    #检查专题课页面元素是否存在
    def zhuanticourseelementcheck(self):
        self.zhuanticourse_page=ZhuantiCoursePage(self.driver)

        len = self.zhuanticourse_page.get_zhuanticoursesubjectchoose_elements()
        if len == 1:
            return True
        elif len == 0:
            return False

    def zhuanticoursetaskcheck(self):
        self.returnindex()
        self.index_handle.click_course1()
        sleep(3)
        self.classdaylist_handle.click_classdaylist3()
        sleep(3)
        self.classdaydetail_handle.clickzhuanticoursetasks()
        sleep(15)
        #手动按压屏幕操作
        TouchAction(self.driver).press(x=200, y=200).release().perform()
        sleep(1)
        try:
            if self.zhuanticourseelementcheck():
                self.driver.keyevent(4)
                sleep(2)
                print("发现题目，返回True，Pass")
                return True
            else:
                self.zhuanticourse_handle=ZhuanticourseHandle(self.driver)
                self.zhuanticourse_handle.click_returnbutton()
                sleep(2)
                print("发现页面返回元素，返回True，Pass")
                return  True
        except:
            print("专题课用例失败")
            return False

        #自我巩固任务检查
    def selfreinforcementtaskscheck(self):
        self.classdaydetail_handle.clickselfreinforcementtasks()
        sleep(2)
        try:
            self.selfreinforcement_page = SelfreinforcementPage(self.driver)
            self.selfreinforcement_page.get_selfreinforcementjifen_elements()
            self.selfreinforcement_handle= SelfreinforcementHandle(self.driver)
            self.selfreinforcement_handle.click_returnbutton()
            sleep(2)
            return  True
        except:
            return False



















        



