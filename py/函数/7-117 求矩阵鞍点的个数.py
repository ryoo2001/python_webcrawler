# 读入矩阵的大小n
n = int(input())

# 创建矩阵
matrix = []

# 读入矩阵
for i in range(n):
    matrix.append([int(x) for x in input().split()])

# 创建一个计数器，用于记录鞍点的个数
count = 0

# 遍历每个元素
for i in range(n):
    for j in range(n):
        # 检查是否是鞍点
        if matrix[i][j] == max(matrix[i]) and matrix[i][j] == min([matrix[x][j] for x in range(n)]):
            # 如果是鞍点，将计数器加1
            count += 1

# 输出鞍点的个数
print(count)