import math

d1 = eval(input())
d2 = eval(input())
r1 = d1 / 2
r2 = d2 / 2
v1 = (4 / 3) * math.pi * r1 ** 3
v2 = (4 / 3) * math.pi * r2 ** 3
c = (v1 + v2) ** (1 / 3)
print(f'正方体边长为:{c:.2f}.')
