from bs4 import BeautifulSoup
import urllib.request, urllib.response, urllib.error
import re
import xlwt


def first_spider():
    print("this is Zhang first web-spider program")
    print("开始爬取....")


def main():
    baseurl = "https://music.douban.com/top250?start="
    patch = "豆瓣音乐top250.xls"
    date = get_data(baseurl)
    save_data(date, patch)


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
        for item in soup.find_all("tr", class_="item"): # 获取音乐信息的页面，提高后期处理效率，排除页面干扰项
            res = {}

            # 获取音乐的链接
            res['link'] =  item.find_all("a")[0]['href'] # 获取标签a的所有内容，在取第一个a标签内的href标签内容
            # 获取图片的链接
            res['imgsrc'] = item.find_all("img")[0]['src'] # 获取标签img的所有内容，在取第一个img标签内的src标签内容
            # 获取音乐的名字
            title = item.select(".pl2 > a")[0] # 获取clss=pl2，子标签为a的内容
            res['title'] = next(title.children).strip() # 处理直接在a标签下的部分音乐名
            alt_title = title.select('span') # 获取大部分在span标签内的音乐名
            if alt_title:
                res['alt_title'] = alt_title[0].get_text().strip() # 使用get_text提取不含标签信息的文本,并使用strip去除头尾空格
            # 获取评分
            res['rate'] = item.select(".rating_nums")[0].get_text().strip() # 查找class=rating_nums内容，get_text提取不含标签信息的文本,并使用strip去除头尾空格
            # 获取评价人数
            rate_count_el = item.select(".star > span.pl")[0] # 查找clss=star为父标签中的<span class="pl">子标签
            res['rate_count'] = re.findall(r'\d+', rate_count_el.get_text())[0]
            # 获取歌手名字
            info_el = item.select("p.pl")[0] # 查找以p标签class=pl的内容
            res['artists'] = info_el.get_text().split("/")[0].strip() # 使用get_text提取不含标签信息的文本，/为分隔符后取第一个元素，去除首尾空格
            print(res)
            # 每一个音乐的信息存入到datalist里面
            datalist.append(res)
    print(len(datalist))
    return datalist


# 保存数据
def save_data(datalist, savepath):
    print("saving....")
    data_excel = xlwt.Workbook(encoding="utf-8", style_compression=0)
    new_excel = data_excel.add_sheet("音乐top250", cell_overwrite_ok=True)
    col = ("音乐链接","图片链接","中文音乐名","别名","评分","评价数","演唱者")
    for k in range(len(col)):
        new_excel.write(0,k,col[k])
    for i in range(0,len(datalist)):
        new_excel.write(i + 1,0,datalist[i]["link"])
        new_excel.write(i + 1,1,datalist[i]["imgsrc"])
        new_excel.write(i + 1,2,datalist[i]["title"])
        if 'alt_title' in datalist[i]:
            new_excel.write(i + 1,3,datalist[i]["alt_title"])
        new_excel.write(i + 1,4,datalist[i]["rate"])
        new_excel.write(i + 1,5,datalist[i]["rate_count"])
        new_excel.write(i + 1,6,datalist[i]["artists"])
    data_excel.save(savepath)
    print("数据保存完成")

if __name__ == "__main__":
    first_spider()
    main()
