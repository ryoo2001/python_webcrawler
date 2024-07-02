n = int(input())
for i in range(n):
    k = int(input())
    lst = []
    for j in range(k):
        a, b, c = input().split()
        lst.append([str(a), int(b), int(c)])
    lst2 = sorted(lst, key=lambda x: (-x[1], -x[2], x[0]))
    order = 0
    for t in range(len(lst2)):
        if t == 0 or lst2[t][1] != lst2[t-1][1] or lst2[t][2] != lst2[t-1][2]:
            order = t + 1
        print(order, *lst2[t])
