tag = True
while tag:
    menu1 = menu
    for key in menu1:
        print(key)
    choice1 = input('第一层>>:').strip()
    if choice1 == 'b':  # 输入b返回上一级
        break
    elif choice1 == 'q':
        tag = False
        continue
    elif choice1 not in menu1:
        continue
    while tag:
        menu2 = menu1[choice1]
        for key in menu2:
            print(key)
        choice2 = input('第二层>>:').strip()
        if choice2 == 'b':  # 输入b返回上一级
            break
        elif choice2 == 'q':
            tag = False
            continue
        elif choice2 not in menu2:
            continue
        while tag:
            menu3 = menu2[choice2]
            for key in menu3:
                print(key)
            choice3 = input('第三层>>:')
            if choice3 == 'b':
                break
            elif choice3 == 'q':
                tag = False
            while tag:
                print(menu3[choice3])
                tag = False
