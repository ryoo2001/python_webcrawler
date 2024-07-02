numble = int(input())
num_1 = numble // 100
num_2 = (numble - num_1 * 100) // 10
num_3 = numble % 10
if num_1**3 + num_2**3 + num_3**3 == numble:
    print("True")
else:
    print("False")