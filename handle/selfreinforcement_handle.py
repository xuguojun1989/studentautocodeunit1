# coding=utf-8
import sys

sys.path.append("..")
from page.selfreinforcement_page import SelfreinforcementPage

class SelfreinforcementHandle:
    def __init__(self,driver):
        self.selfreinforcement_page = SelfreinforcementPage(driver)

    def click_returnbutton(self):
        '''
        点击自我巩固返回按钮
        '''
        self.selfreinforcement_page.get_selfreinforcementreturn_element().click()