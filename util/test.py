import yaml
file_path = '../config/logininfo.yaml'
file=open(file_path)
data = yaml.load(file, Loader=yaml.SafeLoader)
file.close()
print(data)
print(len(data))