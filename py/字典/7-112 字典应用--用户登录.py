dic = {'admin': '123456', 'administrator': '12345678', 'root': 'password'}
for i in range(0, 3):
    name = input()
    password = input()
    if name in dic.keys():
        if dic[name] == password:
            print("登录成功")
            break
        else:
            print("登录失败")
    else:
        print("登录失败")