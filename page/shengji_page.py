#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal

class ShengjiPage:
    #获取升级页面所有页面元素信息
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)


    def get_update_element(self):
        '''
        获取升级页面立即更新按钮元素信息
        '''
        return self.get_by_local.get_element('shengji','update')

    def get_cancel_element(self):
        '''
        获取升级页面取消更新按钮元素信息
        '''
        return self.get_by_local.get_element('shengji','cancel')

    def get_shengjidescribe_element(self):
        '''
        获取升级页面文案元素信息
        '''
        return self.get_by_local.get_element('shengji','shengjidescribe')
