m, n = map(int, input().split())
a = 1
while a <= m:
    b = 1
    while b < n:
        print("*", end="")
        b += 1
    print("*")
    a += 1
