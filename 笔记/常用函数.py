# price = 3.1445
# print('苹果的价格是{}'.format(price))
# print(round(price,2))
# print('苹果的价格是%f'%price)
# print('苹果的价格是%.2f'%price)#保留两位
# print(f'苹果的价格是{price:.3f}')
# a = eval(input())
# print('{:x}'.format(a))
# .split()分割 默认空格 maxsplit=(拆分次数)
# map辅助函数
# map(目标函数，序列)
# xxx.count()指定字符串统计
# isdigit 判断字符串是否为阿拉伯整数
# xxx.isnumeric 判断字符串是否为整数（全世界语言）
# xxx.isalpha 判断是否是常规字符
# xxx.islower 是否小写字符
# xxx.isupper 是否是大写
# xxx.swapcase() 大写转换成小写，小写转换成大写
# xxx.title() 每个单词首字母大写
# xxx.just(补位长度，补位内容）l和r左右
# xxx.center(长度，补位内容) 居中对齐
# xxx.strip()去除内容 有l和r
# xxx.isspace 是否有空格
# str.replace(old, new[, max])
# re.findall(匹配规则，原始文档)
# xxx.startswith(检查字符串是否是以指定子字符串开头)
# xxx.endswith(检查字符串是否是以指定子字符串结尾)
# chr()编码转换字符
# ord()字符转换编码
# "内容".join()，列表转换字符串，内容部分可自定义
# sorted() 任意序列升序，当reverse=True为逆降序(有返回值)
# reverse(),较为特殊的容易，只能赋值一次，有返回值,集合不能使用
# sort() 功能同上，无反回值

# 列表：

# insert(插入位置，内容)
# append(列表末尾插入)
# pop(位置)删除索引位置外的数据
# lambda x:目标函数(x)   类似于map，把列表每个元素进行处理
# 1.与map函数进行使用
# a = map(lambda x:x**2,range(5)) 把0-5（不含5）放入前面函数内计算，并制成列表
# print(list(a))

# 2.lst.sort(key=lambda x:sum(x))  列表中运用，内嵌函数和，比较大小

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(15 // 4)  # 取整
print(15 % 4)  # 取余
print(2 ** 3)  # 幂运算
print(8 ** 1 / 3)  # 三次根号
