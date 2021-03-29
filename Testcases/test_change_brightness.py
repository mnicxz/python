import sys,os
sys.path.append(os.path.dirname(sys.path[0]))

from appium import webdriver
import unittest,time
from Mine.HTMLTestRunner import HTMLTestRunner
from Mine.config import BaseDriver
from Mine.commend import Commend

class test_change_brightness(unittest.TestCase):
    def setUp(self):
        self.basedriver=BaseDriver()
        self.driver = self.basedriver.start_driver()
        print("++++++++++++++++")

    def test_changeBrightness(self):
        Commend.swipe(self.driver,500,22,500,1000,500)
        Commend.swipe(self.driver,200,440,800,440,500)

    #@unittest.skip("临时跳过")
    def tearDown(self):
        #self.driver.find_element_by_text("//*[@text='重置']").click()
        self.driver.quit()

if __name__=='__main__':
    unittest.main()