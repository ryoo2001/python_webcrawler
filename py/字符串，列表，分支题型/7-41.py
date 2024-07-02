a = int(input())
b = list(map(int, input().split()))
b.sort()
if len(b) % 2 == 0:
    m = max(b)
    n = min(b)
    me = b[(len(b) - 1) // 2]
    print(m + n + me)
else:
    m = max(b)
    n = min(b)
    me = b[len(b) // 2]
    print(m + n + me)
