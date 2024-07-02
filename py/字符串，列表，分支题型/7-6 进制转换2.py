i = eval(input())
print(f"{i:x} {i:o} {i:b}")  # f函数格式化输出
print('{:x} {:o} {:b}'.format(i, i, i))  # format格式化输出
print("%x %o" % (i, i))  # %格式化输出
