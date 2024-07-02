def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


def dc(num):
    if num == num[::-1]:
        return True
    else:
        return False


while True:
    try:
        n = input()
        if len(n) < 6 and is_prime(int(n)) and dc(n):
            print("Yes")
        else:
            print("No")
    except:
        break
