a = eval(input())
b = eval(input())
for key, value in a.items():
    if key in b:
        b[key] += value
    else:
        b[key] = value
dic = sorted(zip(b.keys(), b.values()))
d = {}
for i in range(len(dic)):
    d[dic[i][0]] = dic[i][1]
print(d)
