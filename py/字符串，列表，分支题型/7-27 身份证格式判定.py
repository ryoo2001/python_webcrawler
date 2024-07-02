a = input()
ws = a[:17]
if len(a) == 18 and ws.isdigit() == True or a.endswith("X") == True:
    print("True")
else:
    print("False")
