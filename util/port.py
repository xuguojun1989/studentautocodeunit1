#coding=utf-8
from dos_cmd import DosCmd
class Port:
    def prot_is_used(self,port_num):
        '''
        判断端口是否被占用
        '''
        flag =None
        self.dos = DosCmd()
        command = 'netstat -ano | findstr '+port_num
        result = self.dos.excute_cmd_get_result(command)
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag
        
    def create_port_list(self,start_prot,device_list):
        '''
        生成可以端口
        @parameter start_prot
        #parameter device_list
        '''
        port_list = []
        print (device_list)
        if device_list != None:
            while len(port_list) != len(device_list):
                if self.prot_is_used(str(start_prot)) != True:
                    port_list.append(start_prot)
                start_prot = start_prot + 1
            return port_list
        else:
            print ('生成可用端口失败')
            return None
                
            
        
if __name__ == '__main__':
    port = Port()
    li = [1,2,3]
    print (port.create_port_list(1234,li))
      
            
        