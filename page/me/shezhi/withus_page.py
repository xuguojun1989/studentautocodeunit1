#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal

class WithusPage:

    # 获取关于我们所有的页面元素信息
    def __init__(self, driver):
        self.get_by_local = GetByLocal(driver)

    def get_return_element(self):
        '''
        获取返回按钮元素
        '''
        return self.get_by_local.get_element('withuspage','return')
    def get_title_element(self):
        '''
        获取标题按钮
        '''
        return self.get_by_local.get_element('withuspage','title')
    def get_title_element(self):
        '''
        获取标题按钮
        '''
        return self.get_by_local.get_element('withuspage','title')

    def get_userprotocal_element(self):
        '''
        获取用户协议按钮
        '''
        return self.get_by_local.get_element('withuspage','userprotocal')
