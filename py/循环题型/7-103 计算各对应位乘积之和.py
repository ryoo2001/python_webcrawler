a, b = map(int, input().split())
a, b = str(abs(a)), str(abs(b))
la, lb = len(a), len(b)
a = a.rjust(max(la, lb), "0")
b = b.rjust(max(la, lb), "0")
lst = []
for a, b in zip(a, b):
    lst.append(int(a) * int(b))
print(sum(lst))
