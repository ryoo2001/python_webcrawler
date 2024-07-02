def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


def is_symmetry(num):
    lst1 = list(num)
    if len(lst1) == 2 and lst1[0] == lst1[1]:
        return True
    elif len(lst1) == 3 and lst1[0] == lst1[-1]:
        return True
    elif len(lst1) == 4 and lst1[0] == lst1[1] == lst1[2] == lst1[3]:
        return True
    elif len(lst1) == 5 and lst1[0] == lst1[1] == lst1[-1] == lst1[-2]:
        return True
    else:
        return False


while True:
    try:
        n = input()
        k = map(int, n)
        if is_symmetry(k) and is_prime(int(n)):
            print("Yes")
        else:
            print("No")
    except:
        break

