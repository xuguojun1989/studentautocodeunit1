#coding=utf-8
import yaml
class Getuserinfo:
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = '../config/logininfo.yaml'
        else:
            self.file_path = file_path
        self.data = self.read_yaml()
    def read_yaml(self):
        file=open(self.file_path)
        data = yaml.load(file,Loader=yaml.SafeLoader)
        file.close()
        return data
    def get_value(self,section,key):
        try:
            values = self.data[section][key]
        except:
            values = None
        return values
    def get_datalen(self):
        return  len(self.data)