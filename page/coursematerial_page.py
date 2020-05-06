#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal

class CoursematerialPage:
    #获取课程资料页面全部元素
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)

    def get_pdfmaterial_element(self):
        '''
        获取pdf课程资料元素信息
        '''
        return self.get_by_local.get_element('coursematerial','pdf')

    def get_returnbutton_element(self):
        '''
        获取左上角返回按钮元素信息
        '''
        return self.get_by_local.get_element('coursematerial','returnbutton')
