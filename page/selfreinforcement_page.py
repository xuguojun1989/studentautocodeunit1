#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal

class SelfreinforcementPage:
    #获取自我巩固页面全部元素
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)

    def get_selfreinforcementreturn_element(self):
        '''
        获取自我巩固页面返回元素
        '''
        return self.get_by_local.get_element('selfreinforcement','returnbutton')

    def get_selfreinforcementjifen_elements(self):
        '''
        获取自我巩固页面积分元素
        '''
        return self.get_by_local.get_element('selfreinforcement','jifen')