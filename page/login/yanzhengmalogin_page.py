#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal
from base.base_driver import BaseDriver

import time
class Yanzhengmalogin_Page:
    #获取登录页面所有的页面元素信息

    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)

    def get_password_login_element(self):
        '''
        获取密码登录按钮元素信息
        '''
        return self.get_by_local.get_element('yanzhengmalogin','password_login')
    def get_user_protocal_element(self):
        '''
        获取用户协议元素信息
        '''
        return self.get_by_local.get_element('yanzhengmalogin','userprotocal')
    def get_user_hideprotocal_element(self):
        '''
        获取用户隐私协议元素信息
        '''
        return self.get_by_local.get_element('yanzhengmalogin','userhideagrement')
    def get_child_hideprotocal_element(self):
        '''
        获取儿童隐私协议元素信息
        '''
        return self.get_by_local.get_element('yanzhengmalogin','childhideagrement')
