import urllib.error
import urllib.request

# 获取网页

# resource = urllib.request.urlopen(url="http://baidu.com")
# print(resource.status)
# print(resource.getheaders())
# # print(resource.getheaders("Content-Type"))
# html = resource.read().decode("utf-8")
# print(html)

# 模拟浏览器访问

# head = {
#     "User-Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML, likeGecko)Chrome/113.0.0.0Safari / 537.36"
# }
#
# resource = urllib.request.Request(url="https://movie.douban.com/top250", headers=head)
# resourceed = urllib.request.urlopen(resource)
# html = resourceed.read().decode("utf-8")
# print(html)

# 获取网页信息并存储

# head = {
#     "User-Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML, likeGecko)Chrome/113.0.0.0Safari / 537.36"
# }

# resource = urllib.request.Request(url="https://movie.douban.com/top250", headers=head)
# resourceed = urllib.request.urlopen(resource)
# html = resourceed.read().decode("utf-8")
# with open("test.html", mode="w", encoding="utf-8") as file:
#     file.write(html)
