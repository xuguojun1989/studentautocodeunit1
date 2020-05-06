#coding=utf-8
from util.get_user_info import Getuserinfo
class Getuserinfopublic:
    def __init__(self):
        self.get_user_info=Getuserinfo()
    def getusername(self):
        username=self.get_user_info.get_value("user_info_0","username")
        return username
    def getpwd(self):
        pwd=self.get_user_info.get_value("user_info_0","pwd")
        return pwd
    def geterrorpwd(self):
        errorpwd=self.get_user_info.get_value("user_info_0","errorpwd")
        return errorpwd
