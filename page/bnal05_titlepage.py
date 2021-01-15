from selenium.webdriver.common.by import By
from utils.base import BaseObject, BaseHandle
import logging


class TitleObject(BaseObject):
    # 对象层
    def __init__(self):
        super().__init__()
        # 退出
        self.quit_btn_id = (By.ID, "com.yunmall.lc:id/setting_logout")
        # 确认退出
        self.acc_quit_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")

    def find_quit_btn(self):
        # 定位退出
        return self.search_ele(self.quit_btn_id)

    def find_acc_quit_btn(self):
        # 定位确认退出
        return self.search_ele(self.acc_quit_btn_id)


class TitleHandle(BaseHandle):
    # 操作层
    def __init__(self):
        # 实例化对象层
        self.to = TitleObject()

    def click_quit_btn(self):
        # 滑动
        self.screen_swipe()
        logging.info("点击退出")
        # 退出
        self.to.find_quit_btn().click()

    def click_acc_quit_btn(self):
        logging.info("点击确认退出")
        # 确认退出
        self.to.find_acc_quit_btn().click()


class TitleTask:
    logging.info("点击退出")
    # 业务层 实例化操作层
    th = TitleHandle()

    @classmethod
    def logout(cls):
        # 退出
        cls.th.click_quit_btn()
        # 确认退出
        cls.th.click_acc_quit_btn()