a, b = map(int, input().split(","))
if a > 0 and b > 0:
    print("第一象限")
elif a < 0 and b > 0:
    print("第二象限")
elif a < 0 and b < 0:
    print("第三象限")
elif a > 0 and b < 0:
    print("第四象限")
