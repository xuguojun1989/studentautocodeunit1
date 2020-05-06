#coding=utf-8
import sys
sys.path.append("..")
from handle.login.login_handle import LoginHandle
from page.login.login_page import LoginPage
from handle.login.yanzhengmalogin_handle import  YanzhengmaloginHandle
from handle.me.me_handle import MeHandle
from handle.me.set_handle import SetHandle
from handle.index_handle import IndexHandle
from handle.me.shezhi.surelogout_handle import SurelogoutHandle
from page.login.yanzhengmalogin_page import Yanzhengmalogin_Page
from  publicfun.get_userinfopublic import Getuserinfopublic
from  publicfun.check_enterindex import CheckenterIndex
import logging



class LoginBusiness:
    def __init__(self,driver,createdir,username,pwd,errorpwd):
        self.driver=driver
        self.createdir = createdir
        self.get_userinfopublic=Getuserinfopublic()
        self.username=username
        self.pwd=pwd
        self.errorpwd=errorpwd




    # 登陆失败
    def login_mobileorpassword_error(self):
        logging.info('----用例login_mobileorpassword_error执行开始----')
        dir = self.createdir.createcasedir("login_mobileorpassword_error")
        print("创建的目录为" + dir)
        #验证码登陆页面，点击密码登陆
        self.yanzhengmalogin_handle = YanzhengmaloginHandle(self.driver)
        self.yanzhengmalogin_handle.click_passwordlogin()
        #登陆页面输入错误的密码
        self.login_handle = LoginHandle(self.driver)
        #WebDriverWait(self.driver,30, poll_frequency=0.1, ignored_exceptions=None).until(EC.presence_of_element_located((By.ID,'com.gaosi.student:id/et_login_phone')))
        self.login_page = LoginPage(self.driver)
        self.login_page.get_username_element()
        logging.info('获取密码登录页面元素')
        self.login_handle.send_username(self.username)
        self.login_handle.send_password(self.errorpwd)
        #self.driver.keyevent(4)
        self.login_handle.click_login()
        try:
            self.login_page.get_toast_element('手机号或密码错误，请重新输入')
            self.driver.get_screenshot_as_file(dir + '/'+self.username+'login_mobileorpassword_error.png')
            logging.info('----用例login_mobileorpassword_error执行结果True，执行结束----')
            return  True
        except:
            self.driver.get_screenshot_as_file(dir + '/'+self.username+'login_mobileorpassword_error.png')
            logging.info('----用例login_mobileorpassword_error执行结果Flase，执行结束----')
            return  False

    # 登录成功
    def login_pass(self):
        logging.info('----用例login_pass执行开始----')
        dir = self.createdir.createcasedir("login_pass")
        self.login_handle = LoginHandle(self.driver)
        self.login_handle.send_username(self.username)
        self.login_handle.send_password(self.pwd)
        #self.driver.keyevent(4)
        self.login_handle.click_login()
        logging.info('用户名密码登录动作完成')
        #检查是否登录成功
        self.check_enterindex=CheckenterIndex(self.driver)
        if self.check_enterindex.checkenterindex() is True:
            self.driver.get_screenshot_as_file(dir + '/' + self.username + 'login_pass.png')
            logging.info('----用例login_pass执行结果True，执行结束----')
            return True
        else:
            self.driver.get_screenshot_as_file(dir + '/' + self.username + 'login_pass.png')
            logging.info('----用例login_pass执行结果Flase，执行结束----')
            return False

    #退出登陆
    def logoutlogin(self):
        logging.info('----用例logoutlogin执行开始----')
        dir = self.createdir.createcasedir("logoutlogin")
        logging.info('从学习页面开始退出登录页面动作开始')
        self.index_handle=IndexHandle(self.driver)
        self.index_handle.click_lowerbannerme()
        self.me_handle=MeHandle(self.driver)
        self.me_handle.click_set()
        self.set_handel=SetHandle(self.driver)
        self.set_handel.click_cancellogin()
        self.surelogout_handel=SurelogoutHandle(self.driver)
        self.surelogout_handel.click_oklogoutlogin()
        self.yanzhengmalogin_page=Yanzhengmalogin_Page(self.driver)
        logging.info('从学习页面开始退出登录页面动作结束')
        try:
            self.yanzhengmalogin_page.get_password_login_element()
            self.driver.get_screenshot_as_file(dir + '/'+self.username+'logoutlogin.png')
            logging.info('----用例logoutlogin执行结果True，执行结束----')
            return True
        except:
            self.driver.get_screenshot_as_file(dir + '/'+self.username+'logoutlogin.png')
            logging.info('----用例logoutlogin执行结果False，执行结束----')
            return False

