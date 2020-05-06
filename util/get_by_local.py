#coding=utf-8
from .read_ini import ReadIni
class GetByLocal:
    def __init__(self,driver):
        self.driver = driver
    def get_element(self,section,key):
        #id>com.gaosi.student:id/et_login_phone
        read_ini = ReadIni(section)
        local = read_ini.get_value(section,key)
        print ('local is ',local)
        if local is not None:
            by = local.split('>')[0]
            print (by)
            local_by = local.split('>')[1]
            print (local_by)
            if by == 'id':
                return self.driver.find_element_by_id(local_by)
            elif by == 'className':
                elements = self.driver.find_elements_by_class_name(local_by)
                for ele in elements:
                    print(ele)
                print(len(elements))
                return elements
            elif by == 'android_uiautomator':
                elements = self.driver.find_elements_by_android_uiautomator(local_by)
                for ele in elements:
                    print(ele)
                print(len(elements))
                return elements
            else: 
                return self.driver.find_element_by_class_name(local_by)
        else:
            return None