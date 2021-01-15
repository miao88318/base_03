import logging
# 格式化字符串
fmt = "%(asctime)s-%(levelname)s-[%(filename)s-(%(funcName)s()-:%(lineno)d行)]-%(message)s"
logging.basicConfig(level=logging.DEBUG, format=fmt, filename="./hello.log")


def hello():
    logging.debug("--debug信息")
    logging.info("--info信息")
    logging.warning("--warning信息")
    logging.error("--error信息")
    logging.critical("--critical信息")

hello()
