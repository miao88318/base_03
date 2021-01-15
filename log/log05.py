import logging.handlers
import os
# 格式化字符串

logger = logging.getLogger()

logger.setLevel(logging.INFO)

logPath = "../report" + os.sep + "hm.log"
sh = logging.handlers.TimedRotatingFileHandler(logPath, when="midnight", interval=1,
                                               backupCount=7, encoding="utf-8")

logger.addHandler(sh)


logging.info("info")

logging.error("error")
logging.critical("critical")




