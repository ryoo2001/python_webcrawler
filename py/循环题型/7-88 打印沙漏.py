num = int(input())
for i in range(-(num - 1), num):
    p = num - 1 - abs(i)
    s = abs(i) * 2 + 1
    print(" " * p + "*" * s)
