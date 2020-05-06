#page
import sys
sys.path.append("..")
from util.get_by_local import GetByLocal

class PdfpreviewPage:
    #获取pdf预览页页面全部元素
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)

    def get_pdfpreview_element(self):
        '''
        获取pdf打开元素
        '''
        return self.get_by_local.get_element('pdfpreview','pdf')

    def get_returnbutton_element(self):
        '''
        获取左上角返回按钮元素信息
        '''
        return self.get_by_local.get_element('pdfpreview','returnbutton')
