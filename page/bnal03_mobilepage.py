from selenium.webdriver.common.by import By
from utils.base import BaseObject, BaseHandle
import logging


class MobileObject(BaseObject):
    # 对象层 我 对象库层 继承BaseObject 初始化
    def __init__(self):
        super().__init__()
        # 账号
        self.mobile_btu = (By.ID, "com.yunmall.lc:id/logon_account_textview")
        # 密码
        self.password_btu = (By.ID, "com.yunmall.lc:id/logon_password_textview")
        # 点击登录
        self.login_btu = (By.ID, "com.yunmall.lc:id/logon_button")
        # 关闭登录按钮
        self.close_login_btn = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")

    def find_mobile_btu(self):
        # 账号
        return self.search_ele(self.mobile_btu)

    def find_password_btu(self):
        # 密码
        return self.search_ele(self.password_btu)

    def find_login_btu(self):
        # 点击登录
        return self.search_ele(self.login_btu)

    def find_close_login_btn(self):
        # 定位关闭页面按钮
        return self.search_ele(self.close_login_btn)


# class MobileHandle(BaseHandle):
#     # 操作层 继承base类的 BaseHandle 初始化
#     def __init__(self):
#         # 实例化对象库类
#         self.mo = MobileObject()
#
#     def input_mobile_btu(self, username):
#         # 账号
#         self.input_text(self.mo.find_mobile_btu(), username)
#
#     def input_password_btu(self, password):
#         # 密码
#         self.input_text(self.mo.find_password_btu(), password)
#
#     def input_login_btu(self):
#         # 点击登录
#         self.mo.find_login_btu().click()


class MobileHandle(BaseHandle, MobileObject):
    # 操作层 继承base类的 BaseHandle 初始化
    def __init__(self):
        # 实例化对象库类
        MobileObject.__init__(self)

    def input_mobile_btu(self, username):
        logging.info("账号")
        # 账号
        self.input_text(self.find_mobile_btu(), username)

    def input_password_btu(self, password):
        logging.info("密码")
        # 密码
        self.input_text(self.find_password_btu(), password)

    def input_login_btu(self):
        logging.info("点击登录")
        # 点击登录
        self.find_login_btu().click()

    def click_close_login_btn(self):
        logging.info("点击关闭页面按钮")
        # 点击关闭页面按钮
        self.find_close_login_btn().click()


class MobileTask:
    logging.info("点击账号")
    # 业务层 实例化操作层类
    mh = MobileHandle()

    @classmethod
    def mobile(cls, username, password):
        # 账号
        cls.mh.input_mobile_btu(username)
        # 密码
        cls.mh.input_password_btu(password)
        # 登录
        cls.mh.input_login_btu()

    @classmethod
    def close_login(cls):
        # 关闭页面按钮
        cls.mh.click_close_login_btn()


