# a = (list(map(int,input().split())))
# print(*a,sep=" + ",end=f" = {sum(a)}")

a = input().split()
b = map(int, a)
print(" + ".join(a), f"= {sum(b)}")
