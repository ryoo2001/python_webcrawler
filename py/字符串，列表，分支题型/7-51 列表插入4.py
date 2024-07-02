ls = eval(input())
s = input()
p = int(input())
if p <= len(ls):
    ls.insert(p, s)
    ls.append(s)
    print(ls)
else:
    ls.append(s)
    ls.append(s)
    print(ls)
