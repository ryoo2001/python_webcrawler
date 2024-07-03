
from bs4 import BeautifulSoup
import urllib.request, urllib.response, urllib.error
import re

findLink = re.compile(r'<a href="(.*?)">')
findImSrc = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<a href="https://music.douban.com/subject/\d+/"[^>]*>\s*(.*?)\s*</a>')
findRating = re.compile(r'<span class="rating_nums">(\d+\.\d+)</span>')
findJudge = re.compile(r'<span class="pl">\s*\(\s*(\d+)人评价\s*\)\s*</span>')
# findInq = re.compile(r'<span class="inq">(.*?)</span>')
findBd = re.compile(r'<p class="pl">\s*(.*?)\s*/')


def first_spider():
    print("this is Zhang first web-spider program")
    print("开始爬取....")


def main():
    baseurl = "https://music.douban.com/top250?start="
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
        for item in soup.find_all('tr', class_='item'):
            data = []
            item = str(item)
            # 获取音乐的链接
            link = re.findall(findLink, item)[0]
            data.append(link)
            # 获取图片的链接
            imgsrc = re.findall(findImSrc, item)[0]
            data.append(imgsrc)
            # 获取音乐的名字
            titles = re.findall(findTitle, item)
            if titles:
                ctitle = titles[0] if len(titles) > 0 else ""
                otitle = titles[1].replace("/", "") if len(titles) > 1 else ""
                data.append(ctitle)
                data.append(otitle)
            else:
                data.append("")
            # 获取音乐的评分
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            # 获取音乐的评价数
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)
            # 获取演唱者的名字
            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', "", bd)
            bd = re.sub("/", "", bd)
            data.append(bd.strip())
            print(data)
            # 每一个音乐的信息存入到datalist里面
            datalist.append(data)
    print(len(datalist))
    return datalist


if __name__ == "__main__":
    first_spider()
    main()
