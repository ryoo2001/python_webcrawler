a = float(input())
b = 1
c = 1
num = d = 1
i = 1

while c >= a:
    num *= i
    d *= (i * 2 + 1)
    c = num / d
    b += c
    i += 1
print(f"PI = {b * 2:.5f}")
