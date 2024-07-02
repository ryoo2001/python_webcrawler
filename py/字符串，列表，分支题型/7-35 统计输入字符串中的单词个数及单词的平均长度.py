import re

x = input()
str = re.findall("[a-zA-Z]", x)
word = x.split()
print("{},{:.2f}".format(len(word), len(str) / len(word)))
