from TestRequest import TestGetRequest, TestPostRequest
import xlrd
from testdata.getpath import GetTestDataPath

"""    
    :param test_url: 接口请求地址
    :param test_data: 请求参数
    :param test_headers: 设置的请求头
    :param test_case_id: 测试用例编号
    :param test_case_name: 测试用例名称
    :param expected_code: 返回的状态
    :param expected_response: 期望的返回结果
"""

url = 'http://127.0.0.1:8000'
testdata = xlrd.open_workbook(GetTestDataPath())

"""
使用2.0的xlrd 不支持操作xls格式的文件
先删除已安装的xlrd
pip uninstall xlrd
再安装低版本xlrd搞定
pip install xlrd==1.2.0
也可以用openpyxl代替xlrd打开.xlsx文件
"""
# TODO：有待优化：数据化的还有投票接口的投票对象， 还有测试用例编号和测试用例名称的数据化,在实际工作中针对公司实际情况可以对testdata。xls重新设计即可


def post_vote():
    try:
        table = testdata.sheets()[0]  # 获取第一个sheet表中的数据
        num = 0
        for i in range(3, 8):
            num += 1
            choice = table.cell(i, 1).value
            question_id = table.cell(i, 2).value
            status = table.cell(i, 3).value  # float 类型
            ex = table.cell(i, 4).value

            test_url = url + '/poll/' + str(int(question_id)) + '/vote/'
            test_data = {'choice': int(choice)}
            test_headers = ''
            test_case_id = 'post_vote-{}'.format(num)
            test_case_name = table.cell(i, 0).value
            expected_code = str(int(status))
            expected_response = ex
            result = TestPostRequest(test_url, test_data, test_headers, test_case_id, test_case_name, expected_code,
                                     expected_response)
        print(result)
    except Exception as e:
        print(e)


def get_poll():
    try:
        table = testdata.sheets()[0]  # 获取第一个sheet表中的数据
        num = 0
        for i in range(15, 16):
            num += 1
            status = table.cell(i, 1).value  # float 类型
            ex = table.cell(i, 2).value

            test_url = url + '/poll/'
            test_data = ''
            test_headers = ''
            test_case_id = 'get_poll-{}'.format(num)
            test_case_name = table.cell(i, 0).value
            expected_code = str(int(status))
            expected_response = ex
            result = TestGetRequest(test_url, test_data, test_headers, test_case_id, test_case_name, expected_code,
                                    expected_response, 'status')
        print(result)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    post_vote()
    get_poll()
