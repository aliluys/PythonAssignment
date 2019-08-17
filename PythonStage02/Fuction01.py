# 1写函数，用户传入修改的文件名，与要修改的内容，执行函数完成批了修改操作
def modify(file: object, content: object, new_content: object) -> object:
    """
    :param file: 传入的文件名
    :param content: 要修改的内容
    :param new_content: 要改成的内容
    :return:
    """
    with open(file, 'r', encoding='utf-8') as f:
        file_data = ''
        for line in f:
            if content in line:
                line = line.replace(content, new_content)
            file_data += line
    with open(file, 'w', encoding='utf-8') as f:
        f.write(file_data)
    return


if __name__ == '__main__':
    modify('FuncTest01.txt', '两只小蜜蜂', '三只小蜜蜂')