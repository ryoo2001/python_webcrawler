lst1 = []
for i in range(1000, 10000):
    n1 = i // 1000
    n2 = i // 100 % 10
    n3 = i // 10 % 10
    n4 = i % 10
    if n1 != n2 != n3 != n4 and n1 + n2 + n3 + n4 == 6 and i % 11 == 0:
        lst1.append(i)
print(len(lst1))
print(lst1)
