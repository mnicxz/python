import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))

from Mine.commend import Commend
from Mine.config import BaseDriver
from Mine.HTMLTestRunner import HTMLTestRunner
import unittest
from appium import webdriver

class test_open_bluetooth(unittest.TestCase):
    def setUp(self):
        self.basedriver = BaseDriver()
        self.driver = self.basedriver.start_driver()
        print("++++++++++++++++++++++++++++ 测试开始 +++++++++++++++++++++++++++++++")

    def test_openBluetooth(self):
        Commend.swipe(self.driver, 500, 22, 500, 1000, 500)
        Commend.text_click(self.driver, "蓝牙")
        Commend.text_click(self.driver, "测试log")
        a = Commend.run_adb(
            self.driver, 'adb shell settings get global bluetooth_on').split('\n')
        self.assertEqual(a[0], '1')

    # @unittest.skip("临时跳过")
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
