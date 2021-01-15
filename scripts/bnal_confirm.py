# from page.bnal01_homepage import HomeTask
# from page.bnal02_registerpage import RegisterTask
# from page.bnal03_mobilepage import MobileTask
# from page.bnal04_userpage import UserTask
# from page.bnal05_titlepage import TitleTask
from utils.page import Page
import time

time.sleep(1)
# 点击关闭弹窗
# HomeTask.close_alert()
Page.get_home().close_alert()
time.sleep(1)
# 点击我
# HomeTask.goto_sign()
Page.get_home().goto_sign()
time.sleep(2)
# 点击已有账号去登录
# RegisterTask.close_register()
Page.get_register().close_register()
time.sleep(2)
# 输入账号,密码,点击登录
# MobileTask.mobile("18721145092", "zhu930310")
Page.get_mobile().mobile("18721145092", "zhu930310")
time.sleep(2)
# 获取用户名
# print(UserTask.get_username())
print(Page.get_user().get_username())
# 点击设置
# UserTask.setting_btn()
Page.get_user().setting_btn()
# 点击退出
# TitleTask.logout()
Page.get_title().logout()





