def remoney(num):
    a = int(num // 10)
    b = int(num % 10 / 5)
    c = int(num % 10 % 5)
    print(f"{num} = {a}*10 + {b}*5 + {c}*1")


k = int(input())
for i in range(k):
    remoney(int(input()))
