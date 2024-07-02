n = int(input())
m = input().split()
print(" ".join(m[n - 1:] + m[:n - 1]))
