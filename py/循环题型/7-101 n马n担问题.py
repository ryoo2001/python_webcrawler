def ma(n):
    for x in range(n + 1):
        for y in range(n + 1):
            for z in range(0, n + 1, 2):
                if x + y + z == n and 3 * x + 2 * y + z // 2 == n:
                    print(x, y, z)


try:
    while True:
        n = int(input())
        ma(n)
except Exception:
    pass
