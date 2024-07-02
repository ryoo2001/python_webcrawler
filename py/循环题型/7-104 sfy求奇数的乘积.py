def jsj(lst):
    j = 1
    for i in lst:
        if i % 2 != 0:
            j *= i
    return j


try:
    while True:
        lst = list(map(int, input().split()))
        print(jsj(lst))
except:
    pass
