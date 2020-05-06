#coding=utf-8
import sys
sys.path.append("..")
from page.shengji_page import ShengjiPage

class Shengji():
    def __init__(self,driver):
        self.driver=driver

    def checkshengjistatus(self):
        self.shengji_page = ShengjiPage(self.driver)
        try:
            self.shengji_page.get_update_element()
            return  True
        except:
            return  False

    def existaltershengjifirst(self):
        flag = self.checkloginstatus()
        if flag is False:
            print()





