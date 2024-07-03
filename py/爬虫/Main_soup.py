from bs4 import BeautifulSoup
import urllib.request, urllib.response, urllib.error
import re

findLink = re.compile(r'<a href="(.*?)">')
findImSrc = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(
    r'<a href="https://music.douban.com/subject/\d+/"[^>]*>\s*(.*?)\s*</a>'
)
findRating = re.compile(r'<span class="rating_nums">(\d+\.\d+)</span>')
findJudge = re.compile(r'<span class="pl">\s*\(\s*(\d+)人评价\s*\)\s*</span>')
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
        for item in soup.find_all("tr", class_="item"):
            res = {}

            # 获取音乐的链接
            res['link'] =  item.find_all("a")[0]['href']
            # 获取图片的链接
            res['imgsrc'] = item.find_all("img")[0]['src']

            # # 获取音乐的名字
            title = item.select(".pl2 > a")[0]
            res['title'] = next(title.children).strip()
            alt_title = title.select('span')
            if alt_title:
                res['alt_title'] = alt_title[0].get_text().strip()

            res['rate'] = item.select(".rating_nums")[0].get_text().strip()
            rate_count_el = item.select(".star > span.pl")[0]
            res['rate_count'] = re.findall(r'\d+', rate_count_el.get_text())[0]
            info_el = item.select("p.pl")[0]
            res['artists'] = info_el.get_text().split("/")[0].strip()
            print(res)
            # 每一个音乐的信息存入到datalist里面
            datalist.append(res)
    print(len(datalist))
    return datalist


if __name__ == "__main__":
    first_spider()
    main()
