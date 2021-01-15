import pytest
from utils.driver import Driver
from utils.page import Page
from utils.data import Data
import time
import logging

# class TestLogin:
#     def setup_class(self):
#         # 点击关闭弹窗
#         Page.get_home().close_alert()
#
#     def teardown_class(self):
#         Driver.quit_app_driver()
#
#     # 登录正向用例 1.正确手机号 2.正确昵称 3.手机号首空格 4.正确昵称尾空格 + 正确密码
#     @pytest.mark.parametrize("username, password, expect", [("18721145092", "zhu930310", "miao_0310"),
#                                                             ("miao_0310", "zhu930310", "miao_0310"),
#                                                             (" 18721145092", "zhu930310", "miao_0310"),
#                                                             ("miao_0310 ", "zhu930310", "miao_0310")])
#     def test01_login(self, username, password, expect):
#         # 点击我
#         Page.get_home().goto_sign()
#         time.sleep(1)
#         # 点击已有账号去登录
#         Page.get_register().close_register()
#         time.sleep(1)
#         # 账号和密码,点击登录
#         Page.get_mobile().mobile(username, password)
#         time.sleep(1)
#         # 打印用户名
#         # print(Page.get_user().get_username())
#         assert expect in Page.get_user().get_username()
#         time.sleep(1)
#         # 点击设置
#         Page.get_user().setting_btn()
#         time.sleep(1)
#         # 点击退出
#         Page.get_title().logout()

def value():
    data_list = []
    data = Data.get_json_data("bnal.json")
    for i in data:
        data_list.append((i.get("name"),
                          i.get("password"),
                          i.get("exp"),
                          i.get("tag"),
                          i.get("desc")))
    return data_list


class TestLogin:

    def setup_class(self):
        Page.get_home().close_alert()

    def setup(self):
        Page.get_home().goto_sign()
        Page.get_register().close_register()

    def teardown_class(self):
        Driver.quit_app_driver()

    # @pytest.mark.parametrize("name, password, expect, tag, desc", [("18721145092", "zhu930310", "miao_0310"),
    #                                                                ("miao_0310", "zhu930310", "miao_0310"),
    #                                                                (" 18721145092", "zhu930310", "miao_0310"),
    #                                                                ("miao_0310 ", "zhu930310", "miao_0310"),
    #                                                                ("1872114", "zhu930310", "此用户不存在"),
    #                                                                ("18721145092", "930310", "登录密码错误")])
    @pytest.mark.parametrize("name, password, expect, tag, desc", value())
    def test_login(self, name, password, expect, tag, desc):

        # print("\n当前用例:{}".format(desc))
        logging.info("操作元素:{}".format(desc))

        Page.get_mobile().mobile(name, password)

        if not tag:
            assert expect == Page.get_user().get_username()
            Page.get_user().setting_btn()
            Page.get_title().logout()
        else:
            assert Page.get_mobile().mh.toast_message(expect)
            Page.get_mobile().close_login()
