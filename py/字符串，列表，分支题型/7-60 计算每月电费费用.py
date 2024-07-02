a, b = map(float, input().split())
if a <= 50:
    price = a * 0.53
    print(f"cost = {price:.2f}")
else:
    price = (a - 50) * b + 50 * 0.53
    print(f"cost = {price:.2f}")
