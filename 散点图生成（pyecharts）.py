import sqlite3
from pyecharts.charts import Scatter
from pyecharts import options as opts

# 连接到数据库
conn = sqlite3.connect('website/movie.db')
cursor = conn.cursor()

# 从数据库中读取评分数据
cursor.execute("SELECT rate, COUNT(*) as count FROM movie GROUP BY rate")
data = cursor.fetchall()

conn.close()

# 准备数据
scores = [row[0] for row in data]
counts = [row[1] for row in data]

# 生成散点图
scatter = Scatter()
scatter.add_xaxis(scores)
scatter.add_yaxis("电影数量", counts)
scatter.set_global_opts(
    title_opts=opts.TitleOpts(title="豆瓣评分分布"),
    xaxis_opts=opts.AxisOpts(name="评分"),
    yaxis_opts=opts.AxisOpts(name="电影数量")
)

# 将图表保存为 HTML 文件
scatter.render('website/score_scatter.html')
