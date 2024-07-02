numble = int(input())
num_0 = numble // 1000
num_1 = numble // 100 % 10
num_2 = numble % 100//10
num_3 = numble % 10
if num_0**4 + num_1**4 + num_2**4 + num_3**4 == numble:
    print("True")
else:
    print("False")
