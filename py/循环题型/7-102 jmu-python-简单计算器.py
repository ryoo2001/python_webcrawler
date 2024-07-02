n = int(input())
i = 1
lst = []
try:
    while i <= n:
        a = eval(input())
        lst.append(a)
        i += 1
    for j in lst:
        print("{:.2f}".format(j))
except Exception as ex:
    print(type(ex).__name__)
