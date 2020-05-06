#coding=utf-8
import configparser

#print("sections",read_ini.sections())

#print (read_ini.options(read_ini.sections()[0]))

#print (read_ini.items("login_element"))
read_ini = configparser.ConfigParser()
read_ini.read('../config/LocalElement.ini',encoding='UTF-8')

#print (read_ini.get('login_element','username'))

class ReadIni:
    def __init__(self,section,file_path=None):
        if file_path == None:
            self.file_path = '../config/LocalElement.ini'
        else:
            self.file_path = file_path
        self.data = self.read_ini()
    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path,encoding="UTF-8")
        return read_ini
    def get_value(self,section,key):
        if section == None:
            section = 'login_element'
        try:
            values = self.data.get(section,key)
        except:
            values = None
        return values
#if __name__ == '__main__':
#    read_ini = ReadIni()
#    print (read_ini.get_value('password'))

#read_ini = ReadIni()
#print (read_ini.get_value('course1','course_element'))