import time
import datetime


def log(log_file):

    def write_log(func):

        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = func(*args, *kwargs)
            end_time = time.time()
            spend_time = end_time - start_time
            with open(log_file, 'a', encoding='utf-8') as file:
                file.write('%s函数%s开始执行，耗时%ss\n' % (datetime.datetime.today(), func.__name__, spend_time))
            return res

        return wrapper

    return write_log


@log('log_file.txt')
def count(n):
    for i in range(n):
        '哈哈哈'
    return 1


if __name__ == '__main__':
    count(100000000)
