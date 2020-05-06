#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
class LoginPage:

    #获取密码登录页面所有的页面元素信息
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)
        self.driver=driver


    def get_username_element(self):
        '''
        获取用户名元素信息
        '''
        return self.get_by_local.get_element('login_element','username')
        
    def get_password_element(self):
        '''
        获取密码元素信息
        '''
        return self.get_by_local.get_element('login_element','password')
    
    def get_login_button_element(self):
        '''
        获取登录按钮元素信息
        '''
        return self.get_by_local.get_element('login_element','login_button') 
        
    def get_toast_element(self,message):
        '''
        获取toastelement
        '''
        #toast_element = ("xpath", "//*[contains(@text,"+message+")]")
        toast_element = ("xpath", "//*[contains(@text,'" + message + "')]")
        print(toast_element)
        return WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located(toast_element))

    def get_enteryanzhengmalogin_element(self):
        '''
        获取验证码登录元素信息
        '''
        return self.get_by_local.get_element('login_element','enteryanzhengmalogin')
        
    def get_useragrement_element(self):
        '''
        获取用户协议元素信息
        '''
        return self.get_by_local.get_element('login_element','useragrement')
    
    def get_userhideagrement_element(self):
        '''
        获取用户隐私协议元素信息
        '''
        return self.get_by_local.get_element('login_element','userhideagrement')


        
