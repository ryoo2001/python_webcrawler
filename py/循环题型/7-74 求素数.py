def sushu(a):
    if a > 2:
        for i in range(2, a):
            if a % i == 0:
                print(a, "no")
                break
        else:
            print(a, "yes")
    elif a == 2:
        print(a, "yes")
    else:
        print(a, "no")


b = int(input())
sushu(b)
