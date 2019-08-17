# 2写函数，计算传入字符串中【数字】、【字母】、【空格】以及其他的个数
def count_string(string):
    """
    :param string: 传入的字符串
    :return:
    """
    result = {'数字':0, '字母':0, '空格':0, '其他':0}
    for i in string:
        # print(i)
        if i.isdigit():
            result['数字'] += 1
        elif i == ' ':
            result['空格'] += 1
        elif i.isalpha():
            result['字母'] += 1
        else:
            result['其他'] += 1
    return result


if __name__ == '__main__':
    res = count_string('jiu8ijkjku8u89uijkjku  o9899ijij 9o9***8')
    print(res)