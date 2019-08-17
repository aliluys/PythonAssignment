import os


class Shopping:
    def __init__(self, db_file1, product_file1, name1, pwd1):
        self.user_db = db_file1
        self.product_file = product_file1
        self.name = name1
        self.pwd = pwd1
        self.balance = 0
        self.count = 0
        self.current_user_info = []

    def is_registered(self):
        with open(self.user_db, 'r', encoding='utf-8') as registered_file:
            for line in registered_file:
                if self.name in line:
                    return True
            return False

    def register(self):
        inp = input('You are not registered users, do you want to register?(y/n)>>> ')
        if inp in ['y', 'Y', 'yes', 'Yes']:
            with open(self.user_db, 'a', encoding='utf-8') as register_file2:
                register_file2.write('%s|%s\n' % (self.name, self.pwd))
                register_file2.flush()
                print('Registered!'.center(50, '-'))
                return
        else:
            return

    def login(self):
        if not self.is_registered():
            self.register()
            inp = input('注册成功，你要登录吗？(Y/N)')
            if inp.upper() == 'Y':
                return self.login()
            else:
                return False
        else:
            print('You have already registered.')
            with open(self.user_db, 'r', encoding='utf-8') as read_file:
                for line in read_file:
                    if self.name in line:
                        line = line.strip('\n')
                        user_db_info = line.split('|')
                        user_db_name = user_db_info[0]
                        user_db_pwd = user_db_info[1]
                        break
                    else:
                        continue

            # 没有余额信息，要添加
            if len(user_db_info) == 3:
                user_db_balance = user_db_info[2]
            else:
                while True:
                    user_db_balance = input('请添加余额信息>>')
                    if user_db_balance.isdigit():
                        user_db_balance = int(user_db_balance)
                        break
                    else:
                        continue
            self.balance = user_db_balance

            # 将改变添加到文件中
            with open(self.user_db, 'r', encoding='utf-8') as f1, open('%s.bak' % self.user_db, 'w',
                                                                       encoding='utf-8') as f2:
                for line in f1:
                    if self.name in line:
                        line = line + '|' + str(user_db_balance)
                    f2.write(line)
            os.remove(self.user_db)
            os.rename('%s.bak' % self.user_db, self.user_db)

            if self.pwd == user_db_pwd:
                print('You succeed in logging')
                self.current_user_info = [user_db_name, user_db_pwd, user_db_balance]
                return True
            else:
                if self.count < 3:
                    self.pwd = input('Your password is wrong, please input your password again.')
                    self.count += 1
                    return self.login()
                else:
                    print('You have input wrong password too many times.Programs quit.')
                    return False

    def buy(self):
        cond = self.login()
        if cond:  # 已经登录，开始买东西
            product_list = []
            with open(self.product_file, 'r', encoding='utf-8') as product_file:
                for i, line in enumerate(product_file):
                    line = line.strip('\n')
                    product_list.append(line.split(':'))
            total_cost = 0
            shopping_cart = {}
            while True:
                for i in product_list:
                    print(i)
                inp = input('please input the index or the name of the product you want or input q to quit')
                if inp == 'q':
                    print('购物结束')
                    break
                elif inp.isdigit():
                    inp = int(inp)
                    if inp in range(len(product_list)):
                        price = product_list[inp][1]
                        self.balance -= int(price)
                        product_name = product_list[inp][0]
                        print('你选择了%s' % product_name)
                        if product_name in shopping_cart.keys():
                            shopping_cart[product_name]['count'] += 1
                        else:
                            shopping_cart[product_name] = {'count': 1, 'price': price}
                        continue

                    else:
                        print('Invalid operation.')
                        continue
                elif inp in [i[0] for i in product_list]:
                    price = [i[1] for i in product_list if i[0] == inp][0]
                    self.balance -= int(price)
                    product_name = inp
                    print('你选择了%s，已被加入购物车' % product_name)
                    if product_name in shopping_cart.keys():
                        shopping_cart[product_name]['count'] += 1
                    else:
                        shopping_cart[product_name] = {'count': 1, 'price': price}
                    continue
                else:
                    print('Invalid operation.')
                    continue

            if self.balance > 0:  # 余额大于0
                print('After buying this product, You balance is %s,the product price is%s, you can afford it.' % (
                    self.balance, price))
                for i, key in enumerate(shopping_cart):
                    print('%s%23s%23s%23s%23s' % (
                        i,
                        key,
                        shopping_cart[key]['count'],
                        shopping_cart[key]['price'],
                        shopping_cart[key]['price'] * shopping_cart[key]['count']
                    ))
                    total_cost += int(shopping_cart[key]['price'] * shopping_cart[key]['count'])
                    print('your expense is %s, your balance is %s' % (total_cost, self.balance))
            else:
                print('You cannot afford this product, you lack of %s money' % self.balance)
                return

            choice = input('please confirm your purchase.')
            if choice.upper() == 'Y':
                with open(self.user_db, 'r', encoding='utf-8') as f1, open('%s.swap' % self.user_db, 'w',
                                                                           encoding='utf-8') as f2:
                    for line in f1:
                        if self.name in line:
                            line = line.replace(self.current_user_info[-1], str(self.balance))
                        f2.write(line)
                os.remove(self.user_db)
                os.rename('%s.swap' % self.user_db, self.user_db)
            else:
                print('You have canceled this purchase.')


if __name__ == '__main__':
    name = input('输入你的姓名')
    pwd = input('输入你的密码')
    db_file = input('输入用户数据库文件')
    product_file = input('输入产品数据库')
    a = Shopping(db_file, product_file, name, pwd)
    a.buy()
