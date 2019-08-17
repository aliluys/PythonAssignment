# 3写函数，判断用户传入的对象（字符串、列表、元祖）长度是否大于5
def panduan(x):
    """
    :param x: 传入的对象、元祖，列表
    :return:
    """
    bl = False
    if isinstance(x, (str, list, tuple)):
        length = len(x)
        if length > 5:
            bl = True
        else:
            bl = False
    else:
        return 'cannot judge this type data'
    return bl


if __name__ == '__main__':
    res = panduan(1)
    print(res)
