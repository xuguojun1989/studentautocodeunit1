# coding=utf-8
import sys

sys.path.append("..")
from page.me.shezhi.suggestion_page import SuggestionPage



class SuggestionHandle:
    def __init__(self,driver):
        self.suggestion_page = SuggestionPage(driver)

    # 操作意见反馈页面
    def click_returnbutton(self):
        '''
        点击返回按钮
        '''
        self.suggestion_page.get_return_element().click()

    def click_submitbutton(self):
        '''
        点击提交反馈按钮
        '''
        self.suggestion_page.get_submitbutton_element().click()

    def send_suggestion(self,suggestion):
        '''
        点击提交反馈按钮
        '''
        self.suggestion_page.get_editsuggestion_element().send_keys(suggestion)


