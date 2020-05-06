#coding=utf-8
from handle.login.startcunchualter_handle import StartcunchualterHandle

class Checkcunchuutton:
    def __init__(self,driver):
        self.driver=driver


    def clickokbutton(self):
        self.startcunchualter_handle=StartcunchualterHandle(self.driver)
        self.startcunchualter_handle.click_okbuttonlogin()


