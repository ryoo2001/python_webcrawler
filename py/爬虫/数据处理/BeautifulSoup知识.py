# 导入库
from bs4 import BeautifulSoup

# 创建 beautifulsoup 对象
with open("./test.html", "rb") as file:
    html = file.read()
soup = BeautifulSoup(html,'lxml')
## 也可以直接打开网页
soup1 = BeautifulSoup(open('test.html'))

# 搜索文档
## find_all( name , attrs , recursive , text , **kwargs )
### name参数
soup.find_all("h1") # 查找文档中h1标签内容
soup.find_all(["h1", "h2"]) # 查找文档中h1和h2标签内容
### keyword参数
soup.find_all("h1",class_="Special" ) #查找h1标签中class_="Special" 内容
soup.find_all("div",class_="item") #查找div标签中class_="item"内容