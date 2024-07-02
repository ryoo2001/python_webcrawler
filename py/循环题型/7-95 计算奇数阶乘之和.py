def js(n):
    lst = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            lst.append(i)
    return lst


a = int(input())
t = 1
sum = 0
for k in js(a):
    t = 1
    for j in range(1, k + 1):
        t = t * j
    sum = sum + t
print(f"sum={sum}")
