a = int(input())
for i in range(a):
    lst = list(map(int, input().split()))
    lst1 = lst[1:]
    lst2 = sorted(lst1)
    lst_jisu = [j for j in lst2 if j % 2 != 0]
    lst_ousu = [k for k in lst2 if k % 2 == 0]
    lst3 = lst_jisu + lst_ousu
    print(*lst3)