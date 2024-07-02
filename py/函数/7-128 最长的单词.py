def long(lst):
    for i in lst:
        if not i.isalnum():
            lst = lst.replace(i, " ")
    lst1 = lst.split()
    list2 = sorted(lst1, key=lambda x: len(x), reverse=True)
    return list2[0]


while True:
    try:
        a = input()
        print(long(a))
    except:
        break