import sqlite3
from pyecharts.charts import WordCloud
from pyecharts import options as opts

# 连接到数据库
conn = sqlite3.connect('website/movie.db')
cursor = conn.cursor()

# 从数据库中获取电影名称
cursor.execute("SELECT name_cn FROM movie")
titles = cursor.fetchall()

# 关闭数据库连接
conn.close()

# 处理电影名称，生成词云图数据
title_list = [title[0] for title in titles]
words = " ".join(title_list)
word_list = words.split()
word_freq = {word: word_list.count(word) for word in word_list}

# 创建词云图
wordcloud = WordCloud()
wordcloud.add("", word_freq.items(), word_size_range=[20, 100])
wordcloud.set_global_opts(title_opts=opts.TitleOpts(title="电影词云图"))

# 保存词云图为 HTML 文件
wordcloud.render("website/wordcloud.html")
