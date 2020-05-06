#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal

class UserhideprotocalPage:
    #获取设置用户隐私协议所有的页面元素信息
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)

    def get_return_element(self):
        '''
        获取返回按钮元素信息
        '''
        return self.get_by_local.get_element('userhideprotocal','return')
