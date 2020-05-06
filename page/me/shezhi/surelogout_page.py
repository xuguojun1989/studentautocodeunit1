#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal
from base.base_driver import BaseDriver

import time
class SurelogoutPage:
    #获取登陆失效页面所有的页面元素信息
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)

    def get_oklogoutlogin_element(self):
        '''
        获取确定退出按钮元素
        '''
        return self.get_by_local.get_element('surelogout','okbutton')

    def get_cancellogoutlogin_element(self):
        '''
        获取取消退出按钮元素
        '''
        return self.get_by_local.get_element('surelogout','cancelbuttion')

