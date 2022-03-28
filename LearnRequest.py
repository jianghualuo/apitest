import requests
import json

# 获取某个网页
# url = "http://127.0.0.1:8000/poll/2/vote/?choice=6"
# r = requests.get(url)
# print(r.text)  # <Response [200]>
# print(type(r))  # <class 'requests.models.Response'>
# print(r.status_code)  # 200
#
# # requests.get 提供params来传递参数
# # 注意字典里值为 None 的键都不会被添加到 URL 的查询字符串里
# request1 = requests.get(url="http://httpbin.org/get", params={"key1": "value1", "key2": "value2", "list": [1, 2, 3], "key4": None})
# print(request1.url)  # http://httpbin.org/get?key1=value1&key2=value2&list=1&list=2&list=3


"""
我们能读取服务器的响应内容
response.text
requests 会自动解码来自服务器的内容，大多数Unicode字符集都能被无缝地解码
"""
# request2 = requests.get(url="http://127.0.0.1:8000/poll/")
# print(request2)
# print('编码格式:', request2.content)  # 编码格式  content 返回的是二进制数据
# print('encoding:', request2.encoding)
#
# request2.encoding = 'ISO-8859-1'
# print(request2.text)  # 字符串 text返回的是Unicode数据，文本
#
# print('request2.json---》', request2.json())
# rr = json.loads(request2.text)  # json.loads 将json字符串转化为字典；json.dumps 将字典转化为json字符串  encode() 字符串到字节串  decode 字节串到字符串
# print(type(rr))  # 字典
# print(rr.get("data"))
#
# # 定制请求头
# new_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
# zh = requests.get(url='https://www.zhihu.com', headers=new_header)
# print(zh.text)
# print(zh.status_code)

"""
post请求
发送一些编码为表单形式的数据，类似HTML表单。要实现这个，只需要传递一个字典参数data，在请求发出时会被自动编码为表单形式
data可以传入字典或元组（多个元素使用同一个key时使用）


"""
# data1 = {'key1': 'value1', 'key2': 'value2'}
# data2 = [('key1', 'value1'), ('key1', 'value2')]
# data3 = {'key1': 'value1', 'key2': ['1','2']}
#
# r_post1 = requests.post(url='http://httpbin.org/post', data=data1)
# print('1--->', r_post1.text)
# print(r_post1.status_code)
#
# r_post2 = requests.post(url='http://httpbin.org/post', data=data2)
# print('2--->', r_post2.text)
# print(r_post2.status_code)
# #
# r_post3 = requests.post(url='http://httpbin.org/post', data=data3)
# print('3--->', r_post3.text)
# print(r_post3.status_code)

# vote1 = requests.post(url='http://127.0.0.1:8000/poll/2/vote/', data={'choice': 4})
# print(vote1.text)
#
# vote2 = requests.post(url='http://127.0.0.1:8000/poll/2/vote/', data=(('choice', 4), ('choice', None)))
# print(vote1.text)

# # 可以通过响应response获得很多的属性
# # response = requests.get("http://127.0.0.1:8000/poll/")
# response = requests.get("http://www.baidu.com")
# # 状态码
# print(type(response.status_code), response.status_code)
# # headers 头部信息
# print(type(response.headers), response.headers)
# # cookies
# print(type(response.cookies), response.cookies)
# # url
# print(type(response.url), response.url)
# # history
# print(type(response.history), response.history)
#
# # 状态码判断，requests 附带了一个内置的状态码查询对象
# if response.status_code == requests.codes.ok:
#     print("访问成功")


# # requests 是 post一个多部分编码参数变得简单，文件上传和其他参数类似，构建一个字典然后通过files参数传递
# url = 'http://httpbin.org/post'
# file = {"files": open('test.py', 'rb')}
# r_file = requests.post(url, files=file)
# print(r_file.text)
#
# # 可以显式的设置文件名，文件类型和请求头
# url = 'http://httpbin.org/post'
# files = {'file': ('test.py', open('test.py', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
# r = requests.post(url, files=files)
# print(r.text)
#
# # 可以发送作为文件接收的字符串
# url = 'http://httpbin.org/post'
# files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
# r = requests.post(url, files=files)
# print(r.text)

# # cookie 如果响应中包含一些cookie，可以快速访问他们
# r = requests.get('http://www.baidu.com')
# print(r.cookies)
#
# for key, value in r.cookies.items():
#     print(key + "=" + value)
#
# # 发送cookies到服务器，可以使用cookies参数
# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# response = requests.get(url, cookies=cookies)
# print(response.text)
#
# # Cookie 的返回对象为 RequestsCookieJar，它的行为和字典类似，但接口更为完整，适合跨域名跨路径使用。
# # 还可以把 Cookie Jar 传到 Requests 中：
# jar = requests.cookies.RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# url = 'http://httpbin.org/cookies'
# response = requests.get(url, cookies=jar)
# print(response.text)

"""
重定向与请求历史
1.默认情况下，除了head。requests会自动处理重定向
2.可以使用响应对象的history方法来追踪重定向
3.response.history 是一个response对象的列表。从老到近进行排序
如果使用的是get、options、post、put、patch、delete。可以通过allow_redirects 参数禁用重定向处理
如果使用了 HEAD，也可以启用重定向：
"""
# response = requests.get('http://github.com')
# print(response.url)  # github 会把所有http请求重定向为https https://github.com/
# print(response.status_code)  # 200
# print(response.history)  # [<Response [301]>]
#
# r = requests.get('http://github.com', allow_redirects=False)
# print(r.url)
# print(r.status_code)
# print(r.history)

"""
超时
响应超时
经过以timeout参数设定的秒数时间后，停止等待响应；
所有的生产代码都应该使用这一参数，如果不使用，程序可能会永远失去响应
timeout仅对连接过程有效，与响应体的下载无关。如果服务器在timeout秒内没有应答将会引发一个异常
"""
# response = requests.get('http://github.com', timeout=0.1)
# print(response)

# response1 = requests.get('http://github.com', timeout=100)
# print(response1)

"""
错误与异常
1.遇到网络问题，如DNS查询失败，拒绝连接等，requests会抛出一个ConnectionError异常
2.如果http请求返回了不成功的状态码，response。raise_for_status()会抛出一个HttpError异常
3.若请求超时会抛出timeout异常
4.弱请求超过了设定的最大重定向次数，会抛出一个TooManyRedirects
5.所有requests显示抛出的异常都继承自requests.exceptions.RequestException
"""

"""
会话对象session
"""

"""
请求与响应对象
任何时候对于requests.get()的调用， 都在做两件主要的事情。
其一，构建request对象
其二，一旦requests得到服务器的响应，就会产生一个response对象，该响应对象包含服务器返回的所有信息，也包含request对象。
"""
# response = requests.post('http://127.0.0.1:8000/poll/')
# # print('响应的头部信息：', response.headers)
# # print('请求的头部信息：', response.request.headers)
# print(response.text)
# print(type(response.text))
# r = json.loads(response.text)
# print(type(r))
# # print(response.request.url)

r = requests.get(url='http://127.0.0.1:8000/poll/1/vote/', params={'choice': 2})
print(r.text)

# post方法使用data 传参， get方法通过params 传参








# 各种请求
# r1 = requests.post(url="http://127.0.0.1:8000/poll/2/vote/", data={'choice': 5})
# print(r1)
