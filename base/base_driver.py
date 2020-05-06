#coding=utf-8
import time
from appium import webdriver
class BaseDriver:
    def android_driver(self):
        #devices_name
        #prot
        capabilities = {
            "deviceName": "d88590a0",
            "platformVersion": "9",
            #"automationName":"Appium",
            "platformName": "Android",
            "autoAcceptAlerts":True,
            "noReset": True,
            "appPackage": "com.gaosi.student",
            "appActivity": "com.gaosi.student.ui.loading.SplashingActivity",
            "app": "C:\\Users\\xuguo\Desktop\\Android-student-1.2.0.apk",
            "automationName":'UiAutomator2',
            #"fullReset":False
        }
        driver=webdriver.Remote("http://localhost:4723/wd/hub",capabilities)
        #driver.switch_to.alert.accept()
        driver.implicitly_wait(5)
        return driver
    
    def ios_driver(self):
        pass
    def get_driver(self):
        pass