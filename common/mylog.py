import logging
import os
import time
class LogGen():
    def __init__(self,loggerinfo,logname):
        self.logger = logging.getLogger(loggerinfo)
        self.logger.setLevel(logging.INFO)

        #lt=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        #logname=os.path.dirname(os.path.abspath('.'))+'\\logs\\'+lt+'.log'

        fileh=logging.FileHandler(logname)
        fileh.setLevel(logging.INFO)

        consoleh=logging.StreamHandler()
        consoleh.setLevel(logging.INFO)

        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        fileh.setFormatter(formatter)
        consoleh.setFormatter(formatter)

        self.logger.addHandler(fileh)
        self.logger.addHandler(consoleh)

    def getLog(self):
        return self.logger

if __name__ == '__main__':
    lt = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    logname = os.path.dirname(os.path.abspath('.')) + '\\logs\\' + lt + '.log'

    mylogging=LogGen("testing",logname).getLog()
    mylogging.info('aaa')
    mylogging.info('bbb')