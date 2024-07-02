num = int(input())
# 控制空格数量
for i in range(-(num // 2), num // 2 + 1):
    # 输出空格，且不换行
    print((abs(i) + 1) * ' ', end='')
    # 控制”*“输出数量，完成一次换行
    print('*' * (2 * (num // 2 - abs(i)) + 1))
