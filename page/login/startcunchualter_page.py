#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal

import time
class StartcunchualterPage:
    #获取存储权限页面所有页面元素信息
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)

    def get_okbutton_element(self):
        '''
        获取确定元素信息
        '''
        return self.get_by_local.get_element('cunchualter','okbutton')