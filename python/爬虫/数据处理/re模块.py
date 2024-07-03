# Part1 在正则表达式出现之前的传统判断字符串包含技术

"""
a = "C|C++|Java|Python|C#"
print(a.index("Python") > -1)
print("Python" in a)
"""

# Part2 使用正则表达式进行判断

"""
import re
a = "C|C++|Java|Python|C#"
r = re.findall("Python", a)
print(r)

r1 = re.findall("Go", a)
print(r1)

a = "C|C++|Java|Python|C#"
r = re.findall("C", a)
print(r)
"""

# Part3 普通字符匹配

"""
import re

a = 'adhGeu2jf3+=dj6*&fa90@4'
r = re.findall('[0-9]', a)
print(r)

r = re.findall('[a-z]', a)
print(r)

r = re.findall('[A-Z]', a)
print(r)

r = re.findall('[Asu]', a)
print(r)
"""

# Part4 元字符

"""
import re
a = 'adhGeu2jf3+=dj6*&fa90@4'
r = re.findall('[0-9a-zA-Z!%^&]', a)
print(r)

r = re.findall('\d', a)
print(r)

r = re.findall('\D', a)
print(r)

r = re.findall('.', a)
print(r)
"""

# Part5: []中括号代表或的作用

"""
import re

# 字符集
s = 'abc,acc,adc,aec,afc,ahc'

# 匹配出acc 或afc
r = re.findall('a[cf]c', s)
print(r)  # ['acc','afc']

# 匹配出除acc和afc以外的字符串
r = re.findall('a[^cf]c', s)
print(r)

# 匹配出c-f中的所有
r = re.findall('a[c-f]c', s)
print(r)
"""

# Part6: {}数字个数匹配

"""
import re

a = 'python 1111 java739php'
r = re.findall('[a-z]{3}', a)
print(r)

import re

a = 'python 1111 java739php'
r = re.findall('[a-z]{3,6}', a)
print(r)

import re

a = 'python 1111 java739php'
r = re.findall('[a-z]{3,6}?', a)
print(r)
"""

# Part7: * + ? 的区别

"""
import re

a = 'pytho1111 python739pythonn^'

r = re.findall('python*', a)
print(r)
r = re.findall('python+', a)
print(r)
r = re.findall('python?', a)
print(r)
"""

# Part8：边界匹配^(开启）和$(结束）

"""
import re

qq = "qq1000001qq"
r = re.findall('\d{4,8}', qq)
print(r)

import re

qq = "qq1000001"
r = re.findall('^\d{4,8}', qq)
print(r)

import re

qq = "qq1000001"
r = re.findall('\d{4,8}$', qq)
print(r)

import re

qq = "qq1000001"
r = re.findall('^\d{4,8}$', qq)
print(r)
"""

# Part9: ()的作用，（）内的内容作为一个整体，是与的意思

"""
import re

a = 'PythonPythonPythonPythonPython'
r = re.findall("(Python){3}", a)
print(r)

import re

a = 'PythonPython'
r = re.findall("(Python){3}", a)
print(r)
"""

# Part10： re.compile的作用

"""
import re

a = 'python 1111 java739php'
r = re.findall('[a-z]{3}', a)
print(r)

findLink = re.compile(r'[a-z]{3}')
r = re.findall(findLink, a)
print(r)
"""

# Part11: 匹配替换，Sub是Substitute替换的意思

"""
import re

a = 'Python293jddjkJava$%PythonPython'
r = re.sub('Python', 'c', a)
print(r)
r = re.sub('Python', 'c', a, 1)
print(r)
"""

# Part12：?的作用，是贪婪模式还是非贪婪模式

"""
import re

a = 'Python293jddjkJava$%PythonPython'
r = re.findall("Py(.*)Python", a)
print(r)

r = re.findall("Py(.*?)Python", a)
print(r)
"""

# 信息提取综合整合

"""
from bs4 import BeautifulSoup
import urllib.request, urllib.response, urllib.error
import re

# 其中bs4和xlwt需要进行安装。
findLink = re.compile(r'<a href="(.*?)">')
findImSrc = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(r'span class="rating_num" property="v:average">(.*?)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*?)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


def first_spider():
    print("this is my first web-spider program")
    print("开始爬取....")


def main():
    baseurl = "https://movie.douban.com/top250?start="
    get_data(baseurl)


# 爬取单个网页的html内容
def ask_url(url):
    head = {
        "User-Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML, likeGecko)Chrome/113.0.0.0Safari / 537.36"
    }
    request = urllib.request.Request(url, headers=head)
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 爬取网页并进行数据解析
def get_data(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = ask_url(url)
        # 2. 解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):
            data = []
            item = str(item)
            # 获取电影的链接
            link = re.findall(findLink, item)[0]
            data.append(link)
            # 获取图片的链接
            imgsrc = re.findall(findImSrc, item)[0]
            data.append(imgsrc)
            # 获取电影的名字
            titles = re.findall(findTitle, item)
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append("")
            # 获取电影的评分
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            # 获取电影的评价数
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)
            # 获取电影的Slogan
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append("")
            # 获取一堆演员的名字
            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', "", bd)
            bd = re.sub("/", "", bd)
            data.append(bd.strip())
            print(data)
            # 每一个电影的信息存入到datalist里面
            datalist.append(data)
    print(datalist)
    print(len(datalist))
    return datalist


if __name__ == "__main__":
    first_spider()
    main()
"""