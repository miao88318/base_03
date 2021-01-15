import pytest
from selenium.webdriver.common.by import By
from utils.base import BaseObject, BaseHandle
from utils.driver import Driver
from page.settingpage import SettingTask
from page.searchpage import SearchTask


class TestSearch:
    def setup_class(self):
        # self.baseobject = BaseObject()
        # self.basehandle = BaseHandle()
        #
        # self.search_btu = (By.ID, "com.android.settings:id/search")
        # self.search_input = (By.ID, "android:id/search_src_text")
        # self.search_result = (By.ID, "com.android.settings:id/title")
        # self.baseobject.search_ele(self.search_btu).click()
        SettingTask.goto_search_page()

    def teardown_class(self):
        Driver.quit_app_driver()

    @pytest.mark.parametrize("data, num", [("1", "休眠"), ("i", "IP地址"), ("m", "MAC地址")])
    def test_search(self, data, num):
        # self.basehandle.input_text(self.baseobject.search_ele(self.search_input), data)
        # res = self.baseobject.search_eles(self.search_result)

        assert num in SearchTask.search(data)



