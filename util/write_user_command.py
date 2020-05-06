#coding=utf-8
import yaml
with open("../config/userconfig.yaml") as fr:
    data = yaml.load(fr,Loader=yaml.FullLoader)
print (data)
print (data['user_info_0']['bp'])