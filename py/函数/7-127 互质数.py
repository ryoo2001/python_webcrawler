def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)


z = int(input())
for k in range(z):
    data = int(input())
    count = 0
    for j in range(data):
        f, g = map(int, input().split())
        if gcd(f, g) == 1:
            count += 1
    print(count)
