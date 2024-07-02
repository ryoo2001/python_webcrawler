def collatz(num):
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        if num != 1:
            print("%d" % num, end=",")
        else:
            print("%d" % num)
