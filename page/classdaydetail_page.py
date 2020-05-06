import sys
sys.path.append("..")
from util.get_by_local import GetByLocal

class ClassdaydetailPage:
    #获取课节详情页所有元素
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)

    def get_lessonnum_element(self):
        '''
        获取讲次名称
        '''
        return self.get_by_local.get_element('classdaydetail','lessonnum')

    def get_playbackstatus_element(self):
        '''
        获取直播回放按钮
        '''
        return  self.get_by_local.get_element('classdaydetail','watchplayback')

    def get_studytasks_element(self):
        '''
        获取学习任务列表
        '''
        return  self.get_by_local.get_element('classdaydetail','studytasks')

    def get_studytaskstitle_element(self):
        '''
        获取学习任务标题列表
        '''
        return  self.get_by_local.get_element('classdaydetail','studytaskstitle')

    def get_returnbutton_element(self):
        '''
        获取左上角返回按钮元素信息
        '''
        return self.get_by_local.get_element('classdaydetail','returnbutton')