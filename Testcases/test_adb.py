import sys,os
sys.path.append(os.path.dirname(sys.path[0]))

from appium import webdriver
import unittest,time
from Mine.HTMLTestRunner import HTMLTestRunner
from Mine.config import BaseDriver
from Mine.commend import Commend

class test_adb(unittest.TestCase):
    def setUp(self):
        self.basedriver=BaseDriver()
        self.driver = self.basedriver.start_driver()

    def test_adb_devices(self):
        a=Commend.run_adb(self.driver,'adb devices | findstr "device"')
        print(a)
        # key=Commend(self.driver)
        # key.run_adb('adb devices | findstr "device"')

    #@unittest.skip("临时跳过")
    def tearDown(self):
        #self.driver.find_element_by_text("//*[@text='重置']").click()
        self.driver.quit()

if __name__=='__main__':
    unittest.main()