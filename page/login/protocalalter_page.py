#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal

import time
class ProtocalalterPage:
    #获取协议弹窗页面所有页面元素信息
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)

    def get_agree_element(self):
        '''
        获取同意元素信息
        '''
        return self.get_by_local.get_element('protocalalter','agree')
    def get_notagree_element(self):
        '''
        获取不同意元素信息
        '''
        return self.get_by_local.get_element('protocalalter','agree')
