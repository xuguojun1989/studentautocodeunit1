#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal
from base.base_driver import BaseDriver

class IndexPage:
    #获取学习首页所有元素
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)

    def get_lowbannerstudy_element(self):
        '''
        获取学习按钮元素信息
        '''
        return self.get_by_local.get_element('index','lowbannerstudy')

    def get_lowbannerme_element(self):
        '''
        获取我的按钮元素信息
        '''
        return self.get_by_local.get_element('index','lowbannerme')

    def get_coursereadstatus_element(self):
        '''
        获取我的课程下在读状态按钮
        '''
        return  self.get_by_local.get_element('index','readstatus')

    def get_coursesubject_element(self):
        '''
        获取我的课程下科目按钮
        '''
        return  self.get_by_local.get_element('index','coursesubject')

    def get_jiekestatus_element(self):
        '''
        获取已结课状态下拉框元素
        '''
        return  self.get_by_local.get_element('index','readstatusjieke',)

    def get_subject_element(self):
        '''
        获取科目列表
        '''
        return  self.get_by_local.get_element('index','subject')

    def get_course_element(self):
        '''获取指定课程【爱学习在线】在线课程（ceshi勿报名春季）'''
        return  self.get_by_local.get_element('index','course')

    def get_course1_element(self):
        '''获取指定课程【爱学习在线】五年级语文培训（ceshi）'''
        return  self.get_by_local.get_element('index','course1')


