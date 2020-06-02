#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


import time
class SetPage:
    #获取设置页面所有的页面元素信息
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)
        self.driver=driver

    def get_cancellogin_element(self):
        '''
        获取退出登录按钮元素信息
        '''
        return self.get_by_local.get_element('set','logoutlogin')

    def get_cancelusername_element(self):
        '''
        获取注销账号按钮元素信息
        '''
        return self.get_by_local.get_element('set','cancelusername')
    def get_cancelusernametext_element(self):
        '''
        获取注销账号按钮元素文案信息
        '''
        return self.get_by_local.get_element('set','cancelusernametext')
    def get_deletecache_element(self):
        '''
        获取清除缓存按钮元素信息
        '''
        return self.get_by_local.get_element('set','deletecache')
    def get_checkversion_element(self):
        '''
        获取检查版本按钮元素信息
        '''
        return self.get_by_local.get_element('set','checkversion')
    def get_protecteye_element(self):
        '''
        获取检查护眼模式按钮元素信息
        '''
        return self.get_by_local.get_element('set','protecteye')
    def get_withus_element(self):
        '''
        获取检查关于我们按钮元素信息
        '''
        return self.get_by_local.get_element('set','withus')

    def get_toast_element(self,message):
        '''
        获取toastelement
        '''
        toast_element = ("xpath", "//*[contains(@text,'" + message + "')]")
        print(toast_element)
        return WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located(toast_element))


    def get_return_element(self):
        '''
        获取返回按钮元素
        '''
        return  self.get_by_local.get_element('set','returnbutton')