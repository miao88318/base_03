from page.bnal01_homepage import HomeTask
from page.bnal02_registerpage import RegisterTask
from page.bnal03_mobilepage import MobileTask
from page.bnal04_userpage import UserTask
from page.bnal05_titlepage import TitleTask


class Page:

    @classmethod
    def get_home(cls):
        return HomeTask

    @classmethod
    def get_register(cls):
        return RegisterTask

    @classmethod
    def get_mobile(cls):
        return MobileTask

    @classmethod
    def get_user(cls):
        return UserTask

    @classmethod
    def get_title(cls):
        return TitleTask