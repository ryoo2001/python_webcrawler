def zero(num):
    if num[0] == 0 and num[1] == 0:
        return False
    else:
        return True


lst = []
try:
    while True:
        a = list(map(int, input().split()))
        if zero(a):
            lst.append(sum(a))
        else:
            for i in lst:
                print(i)
except:
    exit()
