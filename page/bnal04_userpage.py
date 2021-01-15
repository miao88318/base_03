from selenium.webdriver.common.by import By
from utils.base import BaseObject
import logging


class UserObject(BaseObject):
    # # 对象层 我的页面 对象库层 继承BaseObject 初始化
    def __init__(self):
        super().__init__()
        # 用户名
        self.user_id = (By.ID, "com.yunmall.lc:id/tv_user_nikename")
        # 设置
        self.left_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")

    def find_user_id(self):
        # 用户名
        return self.search_ele(self.user_id)

    def find_left_id(self):
        # 设置
        return self.search_ele(self.left_id)


class UserHandle:
    # 操作层
    def __init__(self):
        # 实例化对象层类
        self.uo = UserObject()

    def input_user_name(self):
        name = self.uo.find_user_id().text
        logging.info("用户名:{}".format(name))
        # 用户名
        return name

    def input_left_btn(self):
        logging.info("设置")
        # 设置
        self.uo.find_left_id().click()


class UserTask:
    logging.info("点击设置")
    # 业务层 实例化操作层类
    uh = UserHandle()

    @classmethod
    def get_username(cls):
        # 用户名
        return cls.uh.input_user_name()

    @classmethod
    def setting_btn(cls):
        # 设置
        cls.uh.input_left_btn()

