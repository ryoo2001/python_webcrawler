def jy(lst):
    dic = {}
    for i in lst:
        dic[i] = dic.get(i, 0) + 1
    return dic.items()


a = jy(input().split())
for k in sorted(a, key=lambda k: -k[1]):
    print(*k, sep=":")
