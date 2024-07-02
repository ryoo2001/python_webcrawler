a, b = map(int, input().split())
lst = list(range(1, a + 1))
l = len(lst)
if lst:
    index = (b - 1) % l
    print(lst.pop(index), end="")
    l -= 1
    while lst:
        index = (index + b - 1) % l
        l -= 1
        print("", lst.pop(index), end="")
