#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal

class ZhuantiCoursePage:
    #获取专题课页面全部元素
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)

    def get_zhuanticoursereturn_element(self):
        '''
        获取专题课页面返回元素
        '''
        return self.get_by_local.get_element('zhuanticourse','return')

    def get_zhuanticoursesubjectchoose_elements(self):
        '''
        获取专题课页面题目素
        '''
        return self.get_by_local.get_element('zhuanticourse','subjectchoose')