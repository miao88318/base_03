from selenium.webdriver.common.by import By
from utils.base import BaseObject
import logging


class HomeObject(BaseObject):
    # 首页对象库层 继承BaseObject 初始化
    def __init__(self):
        super().__init__()
        # 点击关闭弹窗
        self.alert_btu = (By.ID, "com.yunmall.lc:id/img_close")
        # 点击我
        self.my_btu = (By.ID, "com.yunmall.lc:id/tab_me")

    def find_alert_btu(self):
        # 点击关闭弹窗
        return self.search_ele(self.alert_btu)

    def find_my_btu(self):
        # 点击我
        return self.search_ele(self.my_btu)


class HomeHandle:
    # 首页操作库层
    def __init__(self):
        # 实例化对象库层类
        self.ho = HomeObject()

    def click_home_btu(self):
        # 点击关闭弹窗
        logging.info("关闭更新弹窗")
        self.ho.find_alert_btu().click()

    def click_my_btu(self):
        # 点击我
        logging.info("点击我")
        self.ho.find_my_btu().click()


class HomeTask:
    # 首页业务类
    logging.info("首页 ")
    # 实例化操作库层类
    hh = HomeHandle()

    @classmethod
    def close_alert(cls):
        # 点击关闭弹窗
        cls.hh.click_home_btu()

    @classmethod
    def goto_sign(cls):
        # 点击我
        cls.hh.click_my_btu()