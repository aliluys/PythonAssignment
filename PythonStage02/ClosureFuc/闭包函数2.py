# 1编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）
# 要求：登陆成功一次，后续的函数都无需在输入用户名和密码；
# 注意，从文件中独处字符串形式的字典，可以用以下方式把字典字符串转化成字符串
# current_user_info = {'name': None}
import time


def auth(file, current_user_info):
    def user_auth(func):

        def wrapper(*args, **kwargs):
            with open(current_user_info, 'r', encoding='utf-8') as login_file:
                for line in login_file:
                    line = line.strip()
                    line = eval(line)
                    now = time.time()
                    if line['name'] and now-line['login_time'] < 1800:
                        print(line['login_time'])
                        print_time = time.localtime(line['login_time'])
                        print('%s 已经登陆过了, 上次登陆时间为%s年%s月%s日%s时%s分%s秒, 没有超时' %
                              (line['name'], print_time.tm_year, print_time.tm_mon, print_time.tm_mday, print_time.tm_hour, print_time.tm_min, print_time.tm_sec))
                        res = func(*args, **kwargs)
                        return res
                    else:
                        continue

            name = input('用户名>>').strip()
            pwd = input('密码>>').strip()

            with open(file, 'r', encoding='utf-8') as f, open(current_user_info, 'a', encoding='utf-8') as f1:
                for line in f:
                    line = line.strip('\n')
                    line = eval(line)
                    if name == line['name'] and pwd == line['pwd']:
                        now = time.time()
                        f1.write(str({'name': name, 'login_time': now}) + '\n')
                        print('登陆成功')
                        res = func(*args, **kwargs)
                        return res
                    else:
                        continue

            print('账号密码错误')
            return -1

        return wrapper

    return user_auth


@auth('zhanghaomima.txt', 'current_user.txt')
def index():
    time.sleep(3)
    print('welcome to index page')


if __name__ == '__main__':
    index()
