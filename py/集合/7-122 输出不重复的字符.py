a = str(input())
a1 = ""
for i in a:
    if i not in a1:
        a1 += i
print(a1[:10])