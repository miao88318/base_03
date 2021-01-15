import logging
# 格式化字符串

logger = logging.getLogger()

logger.setLevel(logging.INFO)

sh = logging.StreamHandler()

logger.addHandler(sh)

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")




