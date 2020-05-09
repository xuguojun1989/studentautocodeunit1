#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal

class SeteyemodeconfirmPage:

    # 获取清除缓存弹窗页面所有的页面元素信息
    def __init__(self, driver):
        self.get_by_local = GetByLocal(driver)

    def get_set_element(self):
        '''
        获取设置按钮元素
        '''
        return self.get_by_local.get_element('eyemodeconfirm','setbutton')
