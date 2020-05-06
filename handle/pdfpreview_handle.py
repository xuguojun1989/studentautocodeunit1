# coding=utf-8
import sys

sys.path.append("..")
from page.pdfpreview_page import PdfpreviewPage

class PdfpreviewHandle:
    def __init__(self,driver):
        self.pdfpreview_page = PdfpreviewPage(driver)

    def click_returnbutton(self):
        '''
        点击pdf预览页返回按钮
        '''
        self.pdfpreview_page.get_returnbutton_element().click()