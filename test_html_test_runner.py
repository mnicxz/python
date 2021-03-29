import sys,os
sys.path.append(os.path.dirname(sys.path[0]))

from appium import webdriver
import unittest
from Mine.HTMLTestRunner import HTMLTestRunner
from Mine.config import BaseDriver
from Mine.commend import Commend
import Testcases

#dir = os.path.abspath(os.path.join(os.getcwd(), "Testcases"))  
dir="D:/chenchen2/桌面/Mine/VsCode/Appium/Test/Testcases"
#print(os.listdir(dir))
def run_single_testcase(single_testcase):
    testunit = unittest.TestSuite()
    testunit.addTest(single_testcase)
    return testunit

def run_multiple_testcase(dir,pattern='test*.py'):
    suite = unittest.TestSuite()    
    dis = unittest.defaultTestLoader.discover(dir, pattern)
    #print(dis)
    suite.addTests(dis)
    return suite

if __name__ == "__main__":


    #全量测试*
    suite=run_multiple_testcase(dir,'test_*.py')


    # #单条测试
    # suite=run_single_testcase(test_adb('test_adb_devices'))

    with open("./result.html", 'wb') as report:
    #fp = open("./result.html", 'wb')
        runner = HTMLTestRunner(
            report, title='Test',verbosity=2, description='testcase')
        runner.run(suite)
        report.close()



#[<unittest.suite.TestSuite tests=[<unittest.suite.TestSuite tests=[]>]