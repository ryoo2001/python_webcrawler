a, b, c, d = map(int, input().split())
if 0 <= a < c <= 24 and b or d <= 60:
    tmin = (c * 60 + d) - (a * 60 + b)
    h = tmin // 60
    m = tmin % 60
    print(f"{h}:{m}")
