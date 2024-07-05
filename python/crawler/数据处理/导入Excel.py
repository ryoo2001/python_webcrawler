import xlrd
import xlwt
# 打开文件
data = xlrd.open_workbook("test.xlsx")

# 读取工作表
exel = data.nsheets

# 选择工作表
sheet = data.sheet_by_index(0)

# 读取单元格数据
cell_value = sheet.cell_value(1,1)

# 遍历行列并输出
for row in range(sheet.nrows): # 行循环，读取行数量
    for col in range(sheet.ncols): # 列循环，读取列数量
        cell_value = sheet.cell_value(row,col) # 读取单元格信息
        # print(f"{row + 1},{col + 1}单元格值为:{cell_value}")

# 创建新的Excel工作表
excel_book = xlwt.Workbook(encoding="utf-8")
new_excel = excel_book.add_sheet("sheet1", cell_overwrite_ok=True)

# 写入数据
new_excel.write(0, 0, "hello")
new_excel.write(1, 0, "word")

# 保存数据
savepatch = r"python\crawler"
excel_book.save(savepatch) #保存文件到savepatch目录下