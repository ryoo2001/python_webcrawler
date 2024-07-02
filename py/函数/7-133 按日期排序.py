import sys

s = sys.stdin.read().split()
print(*sorted(s, key=lambda x: (x[-4:], x[:2], x[3:5])), sep="\n")