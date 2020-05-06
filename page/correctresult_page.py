#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal

class CorrectresultPage:
    #获取批改结果页面所有元素
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)

    def get_teacherremark_element(self):
        '''
        获取老师评语元素信息
        '''
        return self.get_by_local.get_element('correctresult','teacherremark')

    def get_returnbutton_element(self):
        '''
        获取左上角返回按钮元素信息
        '''
        return self.get_by_local.get_element('correctresult','returnbutton')
