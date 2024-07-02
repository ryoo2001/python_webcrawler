# 从标准输入读入矩阵
n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

# 找出矩阵中的逆鞍点
saddle_points = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == max(matrix[i]) and matrix[i][j] == min(row[j] for row in matrix):
            saddle_points.append((i, j, matrix[i][j]))

# 按行号从小到大、同一行内按列号从小到大的顺序输出逆鞍点
if saddle_points:
    for i, j, value in sorted(saddle_points):
        print(value, i, j)
else:
    print("Not")