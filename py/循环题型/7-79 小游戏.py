def game(nsum):
    if nsum % 5 == 0 and nsum % 7 == 0 and nsum % 3 == 0:
        return 1
    else:
        return 0


t = int(input())
k = list(map(int, input().split()))
for i in range(t):
    for j in range(k[0]):
        if game(sum(k[1:])) == 1:
            print("YES")
            break
        else:
            print("NO")
            break
