def lcm(a, b):
    m = a*b
    while a % b:
        a, b = b, a % b
    return m // b


z = int(input())
for i in range(z):
    lst = list(map(int, input().split()))
    lst1 = list(set(lst[1:]))
    c = lcm(lst1[0], lst1[1])
    for k in range(2, len(lst1)):
        c = lcm(c, lst1[k])
    print(c)
