num = int(input())
if num == 1:
    print(num)
else:
    print(str(num) * num)
    for i in range(num - 2):
        print(str(num), str(num), sep="*" * (num - 2))
    print(str(num) * num)
