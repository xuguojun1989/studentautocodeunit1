#coding=utf-8
#知识点：
#unittest的简单使用
#unittest断言的使用
#unittest中case管理
#HTMLTestRunner的使用
import unittest
import HTMLTestRunner
import sys
sys.path.append("..")
from login.login_business import LoginBusiness
from business.course_business import CourseBusiness
from business.classdetail_business import ClassdetailBusiness
from base.base_driver import BaseDriver
from login.protocol_business import ProtocalBusiness
from business.classdaydetail_business import ClassdaydetailBusiness
from util.createdir import CreateDir
from  publicfun.get_userinfopublic import Getuserinfopublic
from datetime import  datetime
from business.me.personalinfo_business import PersonalinfoBusiness
from login.protocalalter_business import ProtocalalterBusiness
from util.createlogdir import CreatelogDir
from business.me.jinbi_business import JinbiBusiness
from business.me.set.deletelocalcache_business import DeletelocalcacheBusiness
from business.me.set.zhuxiaouser_business import ZhuxiaouserBusiness
from business.me.set.seteyemode_business import SeteyemodeBusiness
from business.me.set.withus_business import WithusBusiness
from business.me.suggestion_business import SuggestionBusiness

class CaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(CaseTest):
   
        print ("这个是测试类的classmethod")
        base_driver = BaseDriver()
        createdir = CreateDir()
        createlogdir=CreatelogDir()
        driver = base_driver.android_driver()
        get_userinfopublic=Getuserinfopublic()

        username=get_userinfopublic.getusername()
        pwd=get_userinfopublic.getpwd()
        errorpwd=get_userinfopublic.geterrorpwd()
        createlogdir.createlogdir()

        CaseTest.protocalalter_business=ProtocalalterBusiness(driver,createdir)
        CaseTest.login_business= LoginBusiness(driver,createdir,username,pwd,errorpwd)
        CaseTest.course_business = CourseBusiness(driver)
        CaseTest.classdetail_business = ClassdetailBusiness(driver)
        CaseTest.classdaydetail_business = ClassdaydetailBusiness(driver)
        CaseTest.protocalbusiness=ProtocalBusiness(driver,createdir)
        CaseTest.personalinfo_business=PersonalinfoBusiness(driver,createdir,username)
        CaseTest.jinbi_business=JinbiBusiness(driver,createdir,username)
        CaseTest.deletelocalcache_business=DeletelocalcacheBusiness(driver,createdir,username)
        CaseTest.zhuxiaouser_business=ZhuxiaouserBusiness(driver,createdir,username)
        CaseTest.seteyemode_business=SeteyemodeBusiness(driver,createdir,username)
        CaseTest.withus_business=WithusBusiness(driver,createdir,username)
        CaseTest.suggestion_business=SuggestionBusiness(driver,createdir,username)

    #下边的是实例方法
    def setUp(self):
        print ('this is set up')

    def test_clickprotocalalteragreebutton(self):
        flag=self.protocalalter_business.clickagreebutton()
        print(flag)
        self.assertTrue(flag)

    def test_loginmobileorpassworderror(self):
        #flag = True
        #print ("this is case")
        #httptestrunner这条即使失败了，也会运行下一条
        #self.assertEqual('1','2','数据错误')
        #self.assertNotEqual('1','1')
        #self.assertTrue(flag)
        #检查登陆是否成功
        flag = self.login_business.login_mobileorpassword_error()
        print(flag)
        self.assertTrue(flag)
    #@unittest.skip("CaseTest")
    def test_loginsuccess(self):
        flag = self.login_business.login_pass()
        print(flag)
        self.assertTrue(flag)

    def test_logoutlogin(self):
        flag = self.login_business.logoutlogin()
        print(flag)
        self.assertTrue(flag)

    def test_userprotocal(self):
        flag = self.protocalbusiness.userprotocal()
        print(flag)
        self.assertTrue(flag)

    def test_userhideprotocal(self):
        flag = self.protocalbusiness.userhideprotocal()
        print(flag)
        self.assertTrue(flag)

    def test_courseselect(self):
        flag = self.course_business.jiekeyuwenselect()
        print(flag)
        self.assertTrue(flag)

    def test_classdetailselect(self):
        flag = self.classdetail_business.classdetailselect()
        print(flag)
        self.assertTrue(flag)
    def test_classdetailplayback(self):
        flag = self.classdaydetail_business.checklivestatus()
        print(flag)
        self.assertTrue(flag)

    def test_classdetail91onlinetask(self):
        flag = self.classdaydetail_business.checkteacherremark()
        print(flag)
        self.assertTrue(flag)

    def test_hejiaotaskshow(self):
        flag = self.classdaydetail_business.checkhejiaoshow()
        print(flag)
        self.assertTrue(flag)

    def test_coursematerial(self):
        flag = self.classdaydetail_business.checklivematerial()
        print(flag)
        self.assertTrue(flag)

    def test_zhuanticoursetaskcheck(self):
        flag = self.classdaydetail_business.zhuanticoursetaskcheck()
        print(flag)
        self.assertTrue(flag)

    def test_selfreinforcementtaskscheck(self):
        flag = self.classdaydetail_business.selfreinforcementtaskscheck()
        print(flag)
        self.assertTrue(flag)

    def test_personalinfocheck(self):
        flag = self.personalinfo_business.selcetpersonalinfo()
        self.assertTrue(flag)
    def test_jinbiinfocheck(self):
        flag = self.jinbi_business.selcetjinbiinfo()
        self.assertTrue(flag)

    def test_deletelocalcache(self):
        flag = self.deletelocalcache_business.deletelocalcache()
        self.assertTrue(flag)

    def test_zhuxiaouser(self):
        flag = self.zhuxiaouser_business.checkzhuxiaouserpage()
        self.assertTrue(flag)

    def test_seteyemode(self):
        flag = self.seteyemode_business.seteyemode()
        self.assertTrue(flag)

    def test_withus(self):
        flag = self.withus_business.checkwithuspage()
        self.assertTrue(flag)

    def test_suggestion(self):
        flag = self.suggestion_business.submitsuggestion()
        self.assertTrue(flag)


    def test_02(self):
        print ("this is case")
        self.assertNotEqual('1', '2')
    def tearDown(self):
        print ('this is teardown')

    @classmethod
    def tearDownClass(CaseTest):
        print ("this is class teardown")
        #CaseTest.driver.quit()
        #f = os.popen(r"adb shell dumpsys activity top | findstr ACTIVITY", "r")  # 获取当前界面的Activity
        #current_activity = f.read()
        #f.close()
        #print(current_activity)  # cmd输出结果

        # 用in方法 判断一个字符串是否包含某字符
        #apppackage_name = 'com.gaosi.student'
        #if apppackage_name in current_activity:
        #    CaseTest.driver.quit()
        #else:
        #    pass
#
# def get_suite():
#     suite = unittest.TestSuite()
#     suite.addTest(CaseTest("test_02"))
#     #suite.addTest(CaseTest("test_01"))
#     #unittest.TextTestRunner().run(suite)
#     html_file = "C:/Users/xgj/Desktop/appium+python自编写源码0202/appium+python自编写源码0202/report/report.html"
#     fp = open(html_file,"wb")
#     #HTMLTestRunner已经继承了unittest，可以这样执行
#     HTMLTestRunner.HTMLTestRunner(fp).run(suite)
        
    
if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(CaseTest("test_clickprotocalalteragreebutton"))
    suite.addTest(CaseTest("test_loginmobileorpassworderror"))
    suite.addTest(CaseTest("test_loginsuccess"))
    suite.addTest(CaseTest("test_logoutlogin"))
    suite.addTest(CaseTest("test_userprotocal"))
    suite.addTest(CaseTest("test_userhideprotocal"))
    suite.addTest(CaseTest("test_personalinfocheck"))
    suite.addTest(CaseTest("test_jinbiinfocheck"))
    suite.addTest(CaseTest("test_zhuxiaouser"))
    suite.addTest(CaseTest("test_deletelocalcache"))
    #suite.addTest(CaseTest("test_seteyemode"))
    suite.addTest(CaseTest("test_withus"))
    suite.addTest(CaseTest("test_suggestion"))

    suite.addTest(CaseTest("test_02"))
    html_file = "../report/result/"+datetime.now().strftime("%Y%m%d_%H%M%S")+"report.html"
    fp = open(html_file,"wb")
    #HTMLTestRunner已经继承了unittest，可以这样执行
    HTMLTestRunner.HTMLTestRunner(fp).run(suite)