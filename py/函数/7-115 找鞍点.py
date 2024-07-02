# 读入矩阵
n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

# 遍历每个位置
for i in range(n):
    for j in range(n):
        # 判断是否为鞍点
        is_saddle_point = True
        for k in range(n):
            # 比较与该位置在同一行的其他位置的值
            if matrix[i][k] > matrix[i][j]:
                is_saddle_point = False
                break
            # 比较与该位置在同一列的其他位置的值
            if matrix[k][j] < matrix[i][j]:
                is_saddle_point = False
                break
        # 如果该位置是鞍点，输出结果并退出程序
        if is_saddle_point:
            print(i, j)
            exit()

# 如果没有找到鞍点，输出 NONE
print("NONE")