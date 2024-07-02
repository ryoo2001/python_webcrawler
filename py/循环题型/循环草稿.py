# for循环方法
# lst = []
# for i in range(101):
#     lst.append(i)
# print(sum(lst))
#
# for循环，自定义函数
# def sum_ry(star, end):
#     lst = []
#     for i in range(star, end + 1):
#         lst.append(i)
#     return sum(lst)
#
#
# a, b = map(int, input().split())
# print(sum_ry(a, b))
#
# 使用while循环方法
i = 0
sum_ = 0
while i <= 100:
    sum_ = i + sum_
    i = i + 1
print(sum_)

# while循环，自定函数法
# def sum_ry(star, end):
#     i = star
#     sum_ = star
#     while i <= end:
#         sum_ = i + sum_
#         i = i + 1
#     return sum_
#
#
# a, b = map(int, input().split())
# print(sum_ry(a, b))
