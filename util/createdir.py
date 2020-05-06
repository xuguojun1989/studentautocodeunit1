from datetime import  datetime
import  os
class CreateDir:
    def __init__(self):
        self.str = "../report/screenshot/" + datetime.now().strftime("%Y%m%d_%H%M%S")
        os.makedirs(self.str)

    def createcasedir(self,casename):
        os.mkdir(self.str+"./"+casename)
        dir = self.str+"./"+casename
        return dir
