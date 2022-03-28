import os
import time

"""
python 标准库 os 有操作文件和目录的函数
"""

# # os.sep 获取当前系统使用的目录分隔符
# print(os.sep)  # \
# # os.name 获取当前使用的操作系统（内核）
# print(os.name)
# # os.getcwd() 获取脚本当前的工作路径
# path1 = os.getcwd()
# print(path1)  # F:\apitest
# path2 = os.getcwdb()
# print(path2)  # b'F:\\apitest'
# # os.chdir 修改当前目录
# os.chdir('G:\\')
# print(os.getcwd())
# os.chdir('F:\\apitest')
# # os.getenv() 获取环境变量
# print(os.getenv('path'))
# if 'Python' in os.getenv('path'):
#     print("ok")
# # os.environ 可以获取并修改环境变量
# print(os.environ)
# print(os.environ['MYSQL_HOME'])
# # os.environ['ljh'] = 'C:\\Users'
# # print(os.environ)
# # del os.environ['ljh']
# # print(os.environ)
#
# # 在当前目录下建立一个子文件夹，有同名文件夹存在时会报错;删除一个文件时，不存在也会报错：系统找不到指定文件
# os.mkdir('test_mkdir')
# os.rmdir('test_mkdir')
#
#
# # 列出某目录下所有的目录和文件
# print(os.listdir('G:\\'))

# # os.rename() 修改路径下文件的名字 找不到指定的文件也会报错
# os.rename('test.py', 'test1.py')
# os.rename('test1.py', 'test.py')

# # os.remove() 删除文件
# file = open('test_test.txt', 'w')
# file.close()
# time.sleep(10)
# os.remove('test_test.txt')

# 路径操作
# import os.path as op
# print(op.abspath('test.py'))  # abspath(path) 返回path在当前系统下的绝对路径
# print(op.abspath('..'))
# # os.mkdir('testdata')
# # os.chdir('.\\testdata')
# # file = open('getpath.py', 'w')
# # file.close()
# print(os.getcwd())
# print(os.path.abspath('.\\testdata\\getpath.py'))
# # os.path.relpath 将绝对路径转化为相对路径，只输出从起始文件夹到目标所需要经过的路径
# print(os.path.relpath('F:\\apitest\\testdata\\getpath.py', ''))  # testdata\getpath.py
# print(os.path.relpath('F:\\apitest\\testdata\\getpath.py', 'testdata'))  # getpath.py
# os.path.join(path, *path)
# r1 = os.path.join('test.xls', os.path.abspath('.'), 'test')  # 如果某个部分为绝对路径，那么前面的所有部分会被丢弃
# r2 = os.path.join(os.path.abspath('.'), 'test.xls')
# r3 = os.path.join(os.path.abspath('.'), 'test.xls', '')  # 最后一个部分为空，将以分隔符结尾
# r4 = os.path.join('test1', 'C:', 'test2')
# print(r1, type(r1))
# print(r2)
# print(r3)
# # print(os.path.relpath(r4))
# print(os.path.dirname(__file__))  # 返回path中的目录路径
# print(os.path.dirname('F:\\apitest\\testdata\\getpath.py'))  # F:\apitest\testdata
# ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(ospath)
# print(os.path.join(ospath, "testdata", "test"))

"""
多线程
"""

# import threading
# import time
#
# stime = time.time()  # 返回当前时间以秒为单位
#
#
# def demo1(m):
#     for i in range(1000):
#         print('demo1-->', i+m)
#     time.sleep(2)
#
#
# def demo2(m):
#     for i in range(2000):
#         print('demo2-->', i+m)
#     time.sleep(2)
#
#
# def demo3(m):
#     for i in range(500):
#         print('demo3-->', i+m)
#     time.sleep(2)
#
# # 创建三个线程，将上面定义的方法分别放在3个线程中，然后分别在传入参数
#
#
# t1 = threading.Thread(target=demo1, args=(1,))
# t2 = threading.Thread(target=demo2, args=(2,))
# t3 = threading.Thread(target=demo3, args=(3,))
#
#
# threads = []  # 定义线程组
#
#
# threads.append(t1)
# threads.append(t2)
# threads.append(t3)
#
# for th in threads:
#     th.start()  # 循环启动线程组中的线程
#
#
# # 单个串行需要用6s+
# # t1.start()
# # t1.join()
# # t2.start()
# # t2.join()
# # t3.start()
# # t3.join()
#
#
# # 执行线程等待方法
# for th in threads:
#     th.join()
#
# etime = time.time()
# print("kkkkk", etime - stime)  # 如果不用join方法，主线程不会等待子线程的执行完毕，会马上结束自己的线程

d = {'a': 1}
print("1" + str(d))

import configparser
config = configparser.ConfigParser()
config.read(r'F:\apitest\config\mail.conf')
to_addrs = config.get('SMTP', 'to_addrs')
print(type(to_addrs))

