#思路 课节元素11个
#之后判断第一讲文字为 已下课，用例pass uiauto是检查的当前页面，个数统计不全

#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal

class ClassdaylistPage:
    #获取我的页面所有页面元素信息
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)

    #此方法暂时未使用
    def get_classdayviewgroup_elements(self):
        '''
        获取课程详情页所有的ViewGroup元素信息
        '''
        return self.get_by_local.get_element('classdaylist','classday')

    def get_coursedaystatus_elements(self):
        '''
        获取课节状态元素信息
        '''
        return  self.get_by_local.get_element('classdaylist','coursedaystatus')

    def get_returnbutton_element(self):
        '''
        获取左上角返回按钮元素信息
        '''
        return self.get_by_local.get_element('classdaylist','returnbutton')
