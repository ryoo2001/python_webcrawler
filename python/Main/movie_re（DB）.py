from bs4 import BeautifulSoup
import urllib.request, urllib.response, urllib.error
import re
import sqlite3


findLink = re.compile(r'<a href="(.*?)">')
findImSrc = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(r'span class="rating_num" property="v:average">(.*?)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*?)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


def first_spider():
    print("this is Zhang first web-spider program")
    print("开始爬取....")


def main():
    baseurl = "https://movie.douban.com/top250?start="
    date = get_data(baseurl)
    insert_data(date)


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
    print("数据解析完成")
    return datalist


# 创建数据库
def new_database():
    conn = sqlite3.connect('movie.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS music (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT,
            imgsrc TEXT,
            name_cn TEXT,
            name_en TEXT,
            rate TEXT,
            rate_count INTEGER,
            summary TEXT
            info TEXT
        )
    ''')
    conn.commit()
    conn.close()


# 数据保存入数据库
def insert_data(datalist):
    conn = sqlite3.connect('movie.db')
    cursor = conn.cursor()
    for data in datalist:
        cursor.execute('''
        INSERT INTO movie (link, imgsrc, name_cn, name_en, rate, rate_count, summary, info)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    first_spider()
    main()
