import os
import time


def GetTestDataPath():
    """

    :return: 测试数据所在的绝对路径
    """
    # cur_abs_path = os.path.abspath('.')
    # return os.path.join(cur_abs_path, 'testdata.xlsx')
    path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(path, 'testdata', 'testdata.xls')


def GetTestLogPath():
    path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(path, 'logs', '{}log.txt'.format(time.strftime("%Y_%m_%d_%H_%M_%S_")))
    # return os.path.join(path, 'logs', 'log.txt')


def GetTestConfig(configname):
    path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(path, 'config', configname)


def GetTestReport():
    path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(path, 'testreport', '{}TestReport.xls'.format(time.strftime("%Y_%m_%d_%H_%M_%S_")))


if __name__ == '__main__':
    print(GetTestDataPath())
    print(GetTestLogPath())
    print(GetTestConfig('config.conf'))
    print(GetTestReport())




