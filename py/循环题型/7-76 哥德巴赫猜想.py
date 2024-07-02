# 1.判断素数
# 2.提取全部素数
# 3.判断每个相乘是否等于输入值
#
# def sushu(n):
#     for num in range(2, int(n**0.5) + 1):
#         if n % num == 0:
#             return False
#     else:
#         return True
#
#
# def sum_susu(a):
#     lst = []
#     for i in range(2, a):
#         if sushu(i):
#             lst.append(i)
#     return lst
#
#
# b = int(input())
# lst = []
# for num in sum_susu(b):
#     for k in sum_susu(b):
#         if b == num + k:
#             lst.append(num)
# # print(lst)
# print(f"{b} = {lst[0]} + {lst[-1]}")
def issusu(n):
    if n > 2:
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False


k = int(input())
for j in range(2, k):
    if issusu(j) and issusu(k - j):
        print(f"{k} = {j} + {k - j}")
        break
