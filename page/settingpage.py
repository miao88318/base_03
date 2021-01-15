from selenium.webdriver.common.by import By
from utils.base import BaseObject


class SettingObject(BaseObject):
    # 继承父类,减少重复实例化和对象调用
    def __init__(self):
        # 对象库层
        super().__init__()
        self.search_btu = (By.ID, "com.android.settings:id/search")

    def find_search_btu(self):
        return self.search_ele(self.search_btu)


class SettingHandle:
    # 操作层
    def __init__(self):
        # 实例化
        self.so = SettingObject()

    def click_setting_btu(self):
        # 点击搜索按钮
        self.so.find_search_btu().click()


class SettingTask:
    # 业务层
    # 实例化
    sh = SettingHandle()

    @classmethod
    def goto_search_page(cls):
        # 进入搜索页面
        cls.sh.click_setting_btu()

