from selenium.webdriver.common.by import By
from utils.base import BaseObject, BaseHandle


class SearchObject(BaseObject):
    # 继承父类,减少重复实例化和对象调用
    # 对象库层
    def __init__(self):
        super().__init__()
        # 搜索输入框
        self.search_input = (By.ID, "android:id/search_src_text")
        # 搜索结果
        self.search_result = (By.ID, "com.android.settings:id/title")

    def find_search_input(self):
        # 定位搜索输入框
        return self.search_ele(self.search_input)

    def find_search_result(self):
        # 定位搜索结果
        return self.search_eles(self.search_result)


class SearchHandle(BaseHandle):
    # 继承父类,减少重复实例化和对象调用
    # 操作层
    def __init__(self):
        super().__init__()
        # 实例化对象库层
        self.so = SearchObject()

    def input_search_text(self, text):
        # 搜索框输入内容
        self.input_text(self.so.find_search_input(), text)

    def get_search_result(self):
        # 返回搜索结果
        res = self.so.find_search_result()
        return [i.text for i in res]


class SearchTask:
    # 实例化操作层
    sh = SearchHandle()

    @classmethod
    def search(cls, text):
        # 输入搜索内容
        cls.sh.input_search_text(text)
        # 返回搜索结果
        return cls.sh.get_search_result()


