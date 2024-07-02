a, b = map(int, input().split())
s = a * b
while a % b != 0:
    a, b = b, a % b
print(b, int(s / b))
