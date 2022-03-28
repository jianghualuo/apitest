import requests
import json
from logs.log import logger

# post_result_list = []
# get_result_list = []
# delete_result_list = []
result_list = []

header = {
    'User-Agent': 'python-requests/2.27.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '8', 'Content-Type': 'application/x-www-form-urlencoded'
}


def TestPostRequest(test_url, test_data, test_headers, test_case_id, test_case_name, expected_code, expected_response):
    """

    :param test_url: 接口请求地址
    :param test_data: 请求参数
    :param test_headers: 设置的请求头
    :param test_case_id: 测试用例编号
    :param test_case_name: 测试用例名称
    :param expected_code: 返回的状态
    :param expected_response: 期望的返回结果
    :return:
    """
    if not test_headers:
        test_headers = header
    logger.info('请求方式：POST')
    logger.info('请求地址：' + test_url)
    logger.info('请求参数：' + str(test_data))
    logger.info('请求头：' + str(test_headers))
    response = requests.post(url=test_url, data=test_data, headers=test_headers)
    result = json.loads(response.text)  # 将json字符串传唤为字典字符串
    response_status = result['status']

    if expected_code == response_status and expected_response in str(result):
        test_result = {
            't_id': test_case_id,
            't_name': test_case_name,
            't_method': 'POST',
            't_url': test_url,
            't_param': '测试数据:' + str(test_data),
            't_expect': 'status:' + expected_code + ' 期望结果：' + expected_response,
            't_actual': 'status:' + response_status + ' 实际结果：' + str(result),
            't_result': '通过'
        }
        logger.info(test_case_id)
        logger.info('通过')
        logger.info('期望返回结果：' + expected_response)
        logger.info('实际返回结果：' + str(result))
    else:
        test_result = {
            't_id': test_case_id,
            't_name': test_case_name,
            't_method': 'POST',
            't_url': test_url,
            't_param': '测试数据:' + str(test_data),
            't_expect': 'status:' + expected_code + ' 期望结果：' + expected_response,
            't_actual': 'status:' + response_status + ' 实际结果：' + str(result),
            't_result': '失败'
        }
        logger.error(test_case_name)
        logger.error('失败')
        logger.error('期望返回结果：' + expected_response)
        logger.error('实际返回结果：' + str(result))

    # post_result_list.append(test_result)
    result_list.append(test_result)
    return result_list


def TestGetRequest(test_url, test_data, test_headers, test_case_id, test_case_name, expected_code, expected_response, st):
    """

    :param test_url: 接口请求地址
    :param test_data: 请求参数
    :param test_headers: 设置的请求头
    :param test_case_id: 测试用例编号
    :param test_case_name: 测试用例名称
    :param expected_code: 返回的状态
    :param expected_response: 期望的返回结果
    :param st:
    :return:
    """
    if not test_headers:
        test_headers = header
    logger.info('请求方式：GET')
    logger.info('请求地址：' + test_url)
    logger.info('请求参数：' + str(test_data))
    logger.info('请求头：' + str(test_headers))
    if test_data:
        response = requests.get(url=test_url, params=test_data, headers=test_headers)
    else:
        response = requests.get(url=test_url, headers=test_headers)
    result = json.loads(response.text)  # 将json字符串传唤为字典字符串
    response_status = result[st]

    if expected_code == response_status and expected_response in str(result):
        test_result = {
            't_id': test_case_id,
            't_name': test_case_name,
            't_method': 'GET',
            't_url': test_url,
            't_param': '测试数据:' + str(test_data),
            't_expect': 'status:' + expected_code + ' 期望结果：' + expected_response,
            't_actual': 'status:' + response_status + ' 实际结果：' + str(result),
            't_result': '通过'
        }
        logger.info(test_case_id)
        logger.info('通过')
        logger.info('期望返回结果：' + expected_response)
        logger.info('实际返回结果：' + str(result))
    else:
        test_result = {
            't_id': test_case_id,
            't_name': test_case_name,
            't_method': 'GET',
            't_url': test_url,
            't_param': '测试数据:' + str(test_data),
            't_expect': 'status:' + expected_code + ' 期望结果：' + expected_response,
            't_actual': 'status:' + response_status + ' 实际结果：' + str(result),
            't_result': '失败'
        }
        logger.error(test_case_name)
        logger.error('失败')
        logger.error('期望返回结果：' + expected_response)
        logger.error('实际返回结果：' + str(result))

    # get_result_list.append(test_result)
    result_list.append(test_result)
    return result_list


def TestDeleteRequest(test_url, test_data, test_headers, test_case_id, test_case_name, expected_code, expected_response):
    """

    :param test_url: 接口请求地址
    :param test_data: 请求参数
    :param test_headers: 设置的请求头
    :param test_case_id: 测试用例编号
    :param test_case_name: 测试用例名称
    :param expected_code: 返回的状态
    :param expected_response: 期望的返回结果
    :return:
    """
    if not test_headers:
        test_headers = header
    logger.info('请求方式：DELETE')
    logger.info('请求地址：' + test_url)
    logger.info('请求参数：' + str(test_data))
    logger.info('请求头：' + str(test_headers))
    response = requests.delete(url=test_url, data=test_data, headers=test_headers)
    result = json.loads(response.text)  # 将json字符串传唤为字典字符串
    response_status = result['status']

    if expected_code == response_status and expected_response in str(result):
        test_result = {
            't_id': test_case_id,
            't_name': test_case_name,
            't_method': 'DELETE',
            't_url': test_url,
            't_param': '测试数据:' + str(test_data),
            't_expect': 'status:' + expected_code + ' 期望结果：' + expected_response,
            't_actual': 'status:' + response_status + ' 实际结果：' + str(result),
            't_result': '通过'
        }
        logger.info(test_case_id)
        logger.info('通过')
        logger.info('期望返回结果：' + expected_response)
        logger.info('实际返回结果：' + str(result))
    else:
        test_result = {
            't_id': test_case_id,
            't_name': test_case_name,
            't_method': 'DELETE',
            't_url': test_url,
            't_param': '测试数据:' + str(test_data),
            't_expect': 'status:' + expected_code + ' 期望结果：' + expected_response,
            't_actual': 'status:' + response_status + ' 实际结果：' + str(result),
            't_result': '失败'
        }
        logger.error(test_case_name)
        logger.error('失败')
        logger.error('期望返回结果：' + expected_response)
        logger.error('实际返回结果：' + str(result))

    # delete_result_list.append(test_result)
    result_list.append(test_result)
    return result_list


if __name__ == '__main__':
    print(TestPostRequest(test_url='http://127.0.0.1:8000/poll/2/vote/', test_data={'choice': 5}, test_headers='', test_case_id='001',
                    test_case_name='投票成功测试', expected_code='200', expected_response="{'status': '200', 'message': 'success'}"))

    # r = requests.post('http://127.0.0.1:8000/poll/2/vote/', data={'choice': 6})
    # print(r.text)
    # print(r.request.headers)
    #
    # d = {"1": 2}
    # print('{"1": 2}' in '{"1": 2}')
