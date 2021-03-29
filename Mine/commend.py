#

import os
from Mine.logger import MyLog

logger=MyLog()


class Commend():

    def __init__(self,driver):
       self.driver=driver

    #滑动
    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        logger.info("执行滑动操作")
        try:
            self.swipe(start_x,start_y,end_x,end_y,duration)
        except Exception as E:
            logger.error("滑动操作失败")
            logger.error(E)

    #通过中文点击
    def text_click(self,text,doc=''):
        #str="//*[text='{}']".format(text)
        logger.info("{0}点击元素：{1}".format(doc, text))
        try:
                self.find_element_by_xpath("//*[@text='{}']".format(text)).click()
        except Exception as E:
            logger.error("点击元素：{}失败!!!".format(text))
            logger.error(E)

    #执行adb指令
    def run_adb(self,adb):
        logger.info("执行{}".format(adb))
        try:
            a = os.popen(adb).read()
            return a
        except Exception as E:
            logger.error("执行失败")
            logger.error(E)