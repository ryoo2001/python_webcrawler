def wanshu(n):
    lst = []
    s = int(n ** 0.5)
    if s ** 2 == n:
        lst.append(s)
    else:
        for i in range(s, 1, -1):
            if n % i == 0:
                lst.insert(0, i)
                lst.append(n // i)
    return sum(lst) + 1 == n


a = int(input())
lst = []
for i in range(6, a + 1):
    if wanshu(i):
        lst.append(i)
print(*lst, sep=',')
