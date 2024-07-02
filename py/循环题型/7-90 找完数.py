import math

l = []
flag = 0
m, n = map(int, input().split())
for i in range(m, n + 1):
    l.append(1)
    for a in range(2, int(math.sqrt(i) + 1)):
        if i % a == 0:
            l.append(a)
            if a * a != 0:
                l.append(i // a)
    if sum(l) == i:
        print("{:d} = ".format(i), end="")
        l.sort()
        print(" + ".join("%s" % id for id in l))
        flag = 1
    l = []
if flag == 0:
    print("None")
