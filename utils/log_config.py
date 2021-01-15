import logging.handlers
import os
# 格式化字符串


def logConfig():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    ls = logging.StreamHandler()

    logPath = "./report" + os.sep + "bnal.log"
    sh = logging.handlers.TimedRotatingFileHandler(logPath, when="midnight", interval=1,
                                                   backupCount=7, encoding="utf-8")

    logger.addHandler(ls)
    logger.addHandler(sh)

    fmt = "%(asctime)s-%(levelname)s-[%(filename)s-(%(funcName)s()-:%(lineno)d行)]-%(message)s"
    formatter = logging.Formatter(fmt)
    sh.setFormatter(formatter)
    ls.setFormatter(formatter)

    logging.debug("-->debug信息")
    logging.info("-->info信息")
    logging.warning("-->warning信息")
    logging.error("-->error信息")
    logging.critical("-->critical信息")


