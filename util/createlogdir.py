from datetime import  datetime
import logging
import  os
class CreatelogDir:

    def createlogdir(self):
        self.filename = '../report/log/' + datetime.now().strftime("%Y%m%d_%H%M%S") + '.log'
        logging.basicConfig(filename=self.filename, level=logging.INFO)
        return self.filename
