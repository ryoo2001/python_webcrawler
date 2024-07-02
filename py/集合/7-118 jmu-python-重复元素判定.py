def cf(n):
    if len(set(n)) == len(n):
        return False
    else:
        return True


k = int(input())
t = 0
f = 0
for i in range(k):
    if cf(list(map(int, input().split()))):
        t = t + 1
    else:
        f += 1
print(f"True={t}, False={f}")
