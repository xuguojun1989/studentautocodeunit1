#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal

class SeteyemodeconfirmPage:

    # 获取设置打开允许再其他应用上 所有的页面元素信息
    def __init__(self, driver):
        self.get_by_local = GetByLocal(driver)

    def get_set_element(self):
        '''
        获取设置按钮元素
        '''
        return self.get_by_local.get_element('eyemodeconfirm','huawei')
    def get_return_element(self):
        '''
        获取返回按钮
        '''
        return self.get_by_local.get_element('eyemodeconfirm','return')
