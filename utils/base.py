from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.driver import Driver
from selenium.common.exceptions import TimeoutException
import time
import logging


class BaseObject:
    def __init__(self):
        self.driver = Driver.get_app_driver()

    def search_ele(self, loc, timeout=5, poll_frequency=1.0):
        logging.info("操作元素:{}".format(loc))
        # 定位单个元素
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(loc[0], loc[1]))

    def search_eles(self, loc, timeout=5, poll_frequency=1.0):
        # 定位一组元素
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(loc[0], loc[1]))


class BaseHandle:
    def input_text(self, ele, text):
        ele.clear()
        ele.send_keys(text)

    def screen_swipe(self, tag=1):
        """
        滑动方法
        :param tag: 1：↑ 2: ↓ 3: ← 4: →
        :return:
        """
        driver = Driver.get_app_driver()
        # 分辨率
        size = driver.get_window_size()
        # 宽
        width = size.get("width")
        # 高
        height = size.get("height")

        # 等待
        time.sleep(1.5)

        if tag == 1:
            # 宽*50%,高*80% -> 宽*50%,高*20%
            logging.info("向上滑动")
            driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 1500)
        if tag == 2:
            logging.info("向下滑动")
            # 宽*50%,高*20% -> 宽*50%,高*80%
            driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, 1500)
        if tag == 3:
            logging.info("向左滑动")
            # 宽*80%,高*50% -> 宽*20%,高*50%
            driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, 1500)
        if tag == 4:
            logging.info("向右滑动")
            # 宽*20%,高*50% -> 宽*80%,高*50%
            driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, 1500)

    def toast_message(self, mess, tag="a"):
        if tag == "a":
            mess = (By.XPATH, "//*[contains(@text, '{}')]".format(mess))
        if tag == "w":
            mess = (By.XPATH, "//*[contains(@text, '{}')]".format(mess))
        try:
            BaseObject().search_ele(mess, 3, 0.3)
            logging.info("toast:{} 存在".format(mess))
            return True
        except TimeoutException:
            logging.info("toast:{} 不存在".format(mess))
            return False
