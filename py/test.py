# import re

# a = 'python 1111 java739php'
# r = re.findall('[a-z]{3,6}?', a) # 贪婪模式（最大）
# print(r)

# a = 'python 1111 java739php'
# r = re.findall('[a-z]{3,6}', a) # 非贪婪模式 （最小）
# print(r)

# a = 'pytho1111 python739pythonn^'
# r = re.findall('python*', a)
# print(r)
# r = re.findall('python+', a)
# print(r)
# r = re.findall('python?', a)
# print(r) 

# import re

# qq = "qq1000001qq"
# r = re.findall('\d{4,8}', qq)
# print(r)

# import re

# qq = "qq1000001"
# r = re.findall('^\d{4,8}', qq)  # '边界匹配，必须以4位或8位开头，
# print(r)

# import re

# qq = "qq1000001"
# r = re.findall('\d{4,8}$', qq) # $ 以4位或者8位数字结束
# print(r)

# import re

# qq = "qq1000001"
# r = re.findall('^\d{4,8}$', qq)
# print(r)

import re

a = 'python 1111 java739php'
r = re.findall('[a-z]{3}', a)
print(r)

findLink = re.compile(r'[a-z]{3}')
r = re.findall(findLink, a)
print(r)