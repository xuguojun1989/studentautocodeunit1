#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class SuggestionPage:

    # 获取意见反馈页面所有元素
    def __init__(self, driver):
        self.get_by_local = GetByLocal(driver)

    def get_return_element(self):
        '''
        获取返回按钮元素
        '''
        return self.get_by_local.get_element('suggestion','return')
    def get_editsuggestion_element(self):
        '''
        获取意见反馈编辑框
        '''
        return self.get_by_local.get_element('suggestion','editsuggestion')
    def get_submitbutton_element(self):
        '''
        获取提交按钮元素
        '''
        return self.get_by_local.get_element('suggestion','submitbutton')

    def get_toast_element(self,message):
        '''
        获取toastelement
        '''
        toast_element = ("xpath", "//*[contains(@text,'" + message + "')]")
        print(toast_element)
        return WebDriverWait(self.driver,10,0.01).until(EC.presence_of_element_located(toast_element))
