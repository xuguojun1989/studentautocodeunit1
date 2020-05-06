#coding=utf-8
from base.base_driver import BaseDriver
class RestartApp:
    def  restartandroid(self):
        self.base_driver=BaseDriver()
        self.base_driver.android_driver()

