year, month, day = map(int, input().split("/"))
lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    lst[1] = 29
    print(sum(lst[:month - 1]) + day)
else:
    print(sum(lst[:month - 1]) + day)
