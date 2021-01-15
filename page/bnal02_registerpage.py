from selenium.webdriver.common.by import By
from utils.base import BaseObject
import logging


class RegisterObject(BaseObject):
    # 首页对象库层 继承BaseObject 初始化
    def __init__(self):
        super().__init__()
        # 点击已有账号去登录
        self.register_btu = (By.ID, "com.yunmall.lc:id/textView1")

    def find_register_btu(self):
        # 返回结果
        return self.search_ele(self.register_btu)


class RegisterHandle:
    # 操作层
    def __init__(self):
        # 实例化对象库层类
        self.ro = RegisterObject()

    def click_register_btu(self):
        logging.info("点击已有账号去登录")
        # 点击已有账号去登录
        self.ro.find_register_btu().click()


class RegisterTask:
    logging.info("点击注册")
    # 实例化操作库层类
    rh = RegisterHandle()

    @classmethod
    def close_register(cls):
        # 点击已有账号去登录
        cls.rh.click_register_btu()