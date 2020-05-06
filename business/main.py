#coding=utf-8
from me.set.zhuxiaouser_business import ZhuxiaouserBusiness
from base.base_driver import BaseDriver
from util.createdir import CreateDir

base_driver = BaseDriver()
driver = base_driver.android_driver()
createdir = CreateDir()
test = ZhuxiaouserBusiness(driver,createdir,'13120391092')
#test.checklivestatus()
#test.checkteacherremark()
print(test.checkzhuxiaouserpage())