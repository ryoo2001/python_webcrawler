def fib(n):
    a, b = 1, 1
    count = 0
    while a <= n:
        print(f"{a:5d}", end="")
        count += 1
        if count % 6 == 0:
            print()
            a, b = b, a + b


fib(int(input()))
