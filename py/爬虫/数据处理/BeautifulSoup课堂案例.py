from bs4 import BeautifulSoup

with open("./test.html", "rb") as file:
    html = file.read()
bs = BeautifulSoup(html, "html.parser")
h2_first_item = bs.find('h2')
print(h2_first_item)

# Part2：BeautifulSoup举例说明2-find_all()方法

with open("py/test.html", "rb") as file:
    html = file.read()
bs = BeautifulSoup(html, "html.parser")
h2_items = bs.find_all('h1')
print(h2_items)

# Part3: BeautifulSoup举例说明3-为查找添加限定条件
from bs4 import BeautifulSoup

with open("./test.html", "rb") as file:
    html = file.read()
bs = BeautifulSoup(html, "html.parser")
h2_items = bs.find_all('li', class_="Special")
print(h2_items)

# Part4: BeautifulSoup举例说明4-提取豆瓣电影Top250的核心信息
with open("./test.html","rb") as file:
    html = file.read()
bs = BeautifulSoup(html, "html.parser")
t_list=bs.find_all("div", class_="item")
print(t_list)