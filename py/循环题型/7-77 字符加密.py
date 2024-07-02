passworld = list(input())
for i in passworld:
    a = ord(i)
    if 97 <= a <= 122:
        print(chr(219 - a), end="")
    elif 65 <= a <= 90:
        print(chr(155 - a), end="")

    else:
        print(chr(a), end="")
