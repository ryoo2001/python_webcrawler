s = list(input())
s1 = input()
p = int(input())
if p <= len(s):
    s.insert(p, s1)
    s.append(s1)
    print(s)
else:
    s.append(s1)
    s.append(s1)
    print(s)
