m = float(input())
if m < 20:
    price = 12 + (m - 1) * 2
    print(int(price + 0.5))
elif 20 <= m < 60:
    price = 39 + (m - 20) * 1.9
    print(int(price + 0.5))
elif m >= 60:
    price = 115 + (m - 60) * 1.3
    print(int(price + 0.5))
