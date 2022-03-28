"""
执行调度模块的实现
"""
from testcase.testvote import *


def demo1():
    post_vote()
    # get_poll()


def demo2():
    get_poll()


"""
当用例量过大时，需要使用多线程并发执行，提升效率
"""


if __name__ == '__main__':
    demo1()
