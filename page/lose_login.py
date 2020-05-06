#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal


import time
class LoseLogin:
    #获取登陆失效页面所有的页面元素信息
    def __init__(self,driver):

        self.get_by_local = GetByLocal(driver)

    def get_loselogin_element(self):
        '''
        获取登录失效确定按钮元素信息
        '''
        return self.get_by_local.get_element('set','cancellogin')
