from appium import webdriver


class BaseDriver:
    def __init__(self, deviceid='4YYDU17313001455', appPackage='com.huawei.android.launcher', appActivity='com.huawei.android.launcher.unihome.UniHomeLauncher'):
        self.deviceid = deviceid
        self.appPackage = appPackage
        self.appActivity = appActivity

    def start_driver(self, port='4723', noreset=True):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "7"
        caps["deviceName"] = self.deviceid
        caps["appPackage"] = self.appPackage
        caps["appActivity"] = self.appActivity
        caps["autoAcceptAlerts"] = True
        caps["autoGrantPermissions"] = True
        caps["noReset"] = True

        driver = webdriver.Remote(
            "http://localhost:{0}/wd/hub".format(port), caps)
        driver.implicitly_wait(10)
        return driver
