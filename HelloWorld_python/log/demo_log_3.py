#encoding=utf8
# 按天生成文件

import logging
import time

from logging.handlers import TimedRotatingFileHandler

#----------------------------------------------------------------------  
if __name__ == "__main__":
    logFilePath = "timed_test.log"
    logger = logging.getLogger("YouLoggerName")
    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler(logFilePath,
                                       when="d",
                                       interval=1,
                                       backupCount=7)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)


    for i in range(6):
        logger.info("This is a info!")
        logger.debug("This is a debug!")
        # time.sleep(61)  