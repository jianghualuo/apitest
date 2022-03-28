import logging
from testdata.getpath import GetTestLogPath


class LogSignleton(object):
    def __init__(self):
        pass

    def get_logger(self):
        # logµÈ¼¶£ºCRITICAL > ERROR > WARNING > INFO > DEBUG
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a,%d %b %Y %H:%M:%S',
                            filename=GetTestLogPath(),
                            filemode='a')
        return logging


logsignleton = LogSignleton()
logger = logsignleton.get_logger()
logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')
