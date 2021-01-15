from appium import webdriver


class Driver:
    __app_driver = None

    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            desired_caps = {
                'platformName': 'Android',  # 平台名字 ios android 不区分大小写
                'platformVersion': '5.1',  # 平台版本 不知道版本写一个空字符串-自动获取版本
                'deviceName': 'aa',  # 设备名字 -不做校验 不能为空
                'appPackage': 'com.yunmall.lc',  # 启动app包名
                'appActivity': 'com.yunmall.ymctoc.ui.activity.MainActivity'  # 启动app启动名 --一般只给首页

            }
            # 声明驱动对象 启动参数指定app自启动  创建session
            cls.__app_driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver:
            cls.__app_driver.quit()
            cls.__app_driver = None

