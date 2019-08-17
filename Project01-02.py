
def shopping():
    with open('RegisteredUserInfo.txt', 'r', encoding='utf-8') as f1, open('BlockedUsers.txt', 'r',
                                                                           encoding='utf-8') as f2:
        data = f1.readlines()
        data = [i.split('|') for i in data]
        RegisteredUsers = [i[0] for i in data]
        RegisteredUsersInfo = {}
        BlockedUsers = [i.strip('\n') for i in f2.readlines()]
        for i in range(len(RegisteredUsers)):
            RegisteredUsersInfo[RegisteredUsers[i]] = {'pwd': data[i][1], 'money': data[i][2].strip('\n')}
        # print(BlockedUsers)

    goods = dict(iphone=1000, macbook=3000, bike=200)
    print('欢迎来到购物商场'.center(50, '-'))
    name = input('请输入账号').strip()
    if name in BlockedUsers:
        print('你在黑名单内，禁止登陆')
        return shopping()
    else:
        if name in RegisteredUsers:
            pwd = input('请输入密码').strip()
            tag = True
            if pwd == RegisteredUsersInfo[name]['pwd']:
                while tag:
                    for i, keys in enumerate(goods.keys()):
                        print(i, ":", keys)
                    choice = input('请输入商品序号或者名称>>').strip()
                    if choice in str(list(range(len(goods)))):
                        choice = list(goods.keys())[int(choice)]
                        price = goods[choice]
                    elif choice in list(goods.keys()):
                        price = goods[choice]
                    else:
                        print('输入了错误的商品名称或序号')
                        continue
                    users_money = int(RegisteredUsersInfo[name]['money'])
                    if users_money >= price:
                        RegisteredUsersInfo[name]['money'] = str(users_money - price)
                        print('你成功购买了%s,花费了%.2f,余额为%.2f' % (
                            choice, goods[choice], users_money - price))
                        file_data = ''
                        with open('RegisteredUserInfo.txt', 'r', encoding='utf-8') as file:
                            for line in file:
                                if name in line and str(users_money) in line:
                                    line = line.replace(str(users_money),
                                                        str(users_money - price))
                                file_data += line
                        with open('RegisteredUserInfo.txt', 'w', encoding='utf-8') as file:
                            file.write(file_data)
                    else:
                        print('余额不足！')

                    while tag:
                        still = input('继续购物吗?Y/N').strip()
                        if still.upper() == 'Y':
                            break
                        elif still.upper() == 'N':
                            tag = False
                        else:
                            still = input('你输入了奇怪的东西，请再次确认').strip()
                            continue
            else:
                count = 3
                while count:
                    pwd = input('密码错误，请重新输入')
                    if pwd == RegisteredUsersInfo[name]['pwd']:
                        return shopping()
                    else:
                        count = count - 1
                        if count == 0:
                            with open('BlockedUsers.txt', 'a', encoding='utf-8') as f:
                                f.write(name + '\n')
                            print('你已被加入黑名单')
                            return shopping()
                        else:
                            continue
        else:
            print('你没有注册，请注册')
            name = input('请输入你的姓名>>').strip()
            pwd = input('请输入你的密码>>').strip()
            money = input('请输入你的充值金额>>').strip()
            with open('RegisteredUserInfo.txt', 'a', encoding='utf-8') as f:
                f.write(name + '|' + pwd + '|' + money + '\n')
            return shopping()


if __name__ == '__main__':
    shopping()
