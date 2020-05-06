#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal

import time
class AgreeornotPage:
    #获取我的页面所有页面元素信息
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)


    def get_set_elements(self):
        '''
        获取我的页面设置按钮元素信息
        '''
        return self.get_by_local.get_element('zhuanticoursealter','agreeornot')
