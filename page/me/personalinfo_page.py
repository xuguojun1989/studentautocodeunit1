#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal

import time
class PersonalinfoPage:
    #获取个人资料页面所有页面元素信息
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)

    def get_name_element(self):
        '''
        获取名字元素信息
        '''
        return self.get_by_local.get_element('personalinfo','name')
    def get_return_element(self):
        '''
        获取返回按钮按钮元素信息
        '''
        return self.get_by_local.get_element('personalinfo','return')
