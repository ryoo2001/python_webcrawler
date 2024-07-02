def fj(num):
    lst = []
    i = 2
    while num > 1:
        if num % i == 0:
            lst.append(i)
            num //= i
        else:
            i += 1
    return lst


n = int(input())
print(*fj(n), end=" ")
