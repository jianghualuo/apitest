"""
定义多线程运行方法，执行测试用例
"""
import threading
import time
from TestAllCass import *


def threads():
    stime = time.time()

    # 定义线程组
    threads = []
    # 将两个测试用例集放入线程组中
    threads.append(threading.Thread(target=demo1))
    threads.append(threading.Thread(target=demo2))

    for th in threads:
        th.start()

    for th in threads:
        th.join()

    etime = time.time()
    print("测试耗时{}秒".format(etime - stime))


if __name__ == '__main__':
    threads()
