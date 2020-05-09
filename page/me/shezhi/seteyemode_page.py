#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal

class SeteyemodePage:

    # 获取清除缓存弹窗页面所有的页面元素信息
    def __init__(self, driver):
        self.get_by_local = GetByLocal(driver)

    def get_ok_element(self):
        '''
        获取确定按钮元素
        '''
        return self.get_by_local.get_element('eyemode', 'okbutton')

    def get_cancel_element(self):
        '''
        获取取消按钮元素
        '''
        return self.get_by_local.get_element('eyemode', 'cancelbutton')
