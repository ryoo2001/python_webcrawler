N = int(input())
n = list(map(int, input().split()))
avg = sum(n) / N
print(f'{(sum(map(lambda k: (k - avg) ** 2, n)) / N) ** 0.5:.5f}')
