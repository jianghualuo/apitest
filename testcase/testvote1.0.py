from TestRequest import TestGetRequest, TestPostRequest

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


def post_vote():
    try:
        test_url = url + '/poll/1/vote/'
        test_data = {'choice': 4}
        test_headers = ''
        test_case_id = '001'
        test_case_name = '测试投票接口'
        expected_code = '200'
        expected_response = "{'status': '200', 'message': 'success'}"
        TestPostRequest(test_url, test_data, test_headers, test_case_id, test_case_name, expected_code,
                        expected_response)
    except Exception as e:
        print(e)


def get_poll():
    try:
        test_url = url + '/poll/'
        test_data = ''
        test_headers = ''
        test_case_id = '001'
        test_case_name = '测试获取所有问题接口'
        expected_code = '200'
        expected_response = 'success'
        TestGetRequest(test_url, test_data, test_headers, test_case_id, test_case_name, expected_code,
                        expected_response, 'status')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # post_vote()
    get_poll()
