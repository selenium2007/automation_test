from script.module import *
import time
import os.path
import unittest
from common.mylog import LogGen
from common.myemail import mysendemail
from HTMLTestRunner import HTMLTestRunner


class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        if not os.path.exists("logs"):
            os.mkdir("logs")
        if not os.path.exists("pic"):
            os.mkdir("pic")


        now = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        logname = os.path.abspath('.') + '\\logs\\' + now + '.log'
        cls.logger=LogGen("mytest", logname).getLog()

    @classmethod
    def tearDownClass(cls):
        pass
        #mysendemail("please find HTML report in /mypro/report directory")


    #@unittest.skip("reason for skipping")
    def test_login(self):
        tcname_dir=os.path.abspath('.')+'\\data\\'
        tcname='login'
        self.assertTrue(readTestCase(tcname_dir,tcname,self.logger))

    #@unittest.skip("reason for skipping")
    def test_register(self):
        tcname_dir = os.path.abspath('.') + '\\data\\'
        tcname = 'register'
        self.assertTrue(readTestCase(tcname_dir, tcname, self.logger))


if __name__ == '__main__':

    suite=unittest.TestSuite()
    suite.addTest(MyTest('test_login'))
    suite.addTest(MyTest('test_register'))

    if not os.path.exists("report"):
        os.mkdir("report")
    now = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    reportfile=os.path.abspath('.')+'\\report\\'+now+'-result.html'
    fh=open(reportfile,"wb")
    runner=HTMLTestRunner(stream=fh,title='test report',description='test cases')
    runner.run(suite)
    fh.close()



