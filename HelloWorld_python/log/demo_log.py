#encoding=utf8

import logging

#默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
# logging.debug('this is debug')
# logging.info('this is info')
# logging.warning('this is warning')
# logging.error('this is error')






def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        filename='D:\\workspace_HelloWorld\\HelloWorld_my\\HelloWorld_python\\selenium_my_\\jingguan.log',
                        filemode='a')
    logging.info('this is info=======================')
    pass


if __name__ == '__main__':
    main()