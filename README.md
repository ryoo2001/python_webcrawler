# python_webcrawler

一个基于 Python 的豆瓣 Top250 数据采集与可视化课程实践项目。项目包含电影、音乐数据爬取示例，支持将数据保存到 Excel 或 SQLite，并通过 Flask + ECharts 页面展示电影列表、评分分布和词云结果。

## 功能概览

- 爬取豆瓣电影 Top250 页面数据
- 爬取豆瓣音乐 Top250 页面数据示例
- 使用 BeautifulSoup 和正则表达式解析网页内容
- 将爬取结果保存为 Excel 文件或 SQLite 数据库
- 使用 pyecharts 生成评分散点图和电影名称词云
- 使用 Flask 启动本地可视化网站
- 保留课程练习、数据处理示例和静态网页模板

## 项目结构

```text
.
+-- app.py                    # 主入口：爬取、入库、生成图表并启动 Flask
+-- analyze_save.py           # 豆瓣电影 Top250 爬取与 SQLite 保存
+-- scatter_diagram.py        # 电影评分分布图生成
+-- cloud.py                  # 电影名称词云生成
+-- web.py                    # Flask 路由与页面服务
+-- python/                   # 课程练习与独立爬虫示例
+-- temp_date/                # 示例数据与历史输出
+-- website/                  # Flask 使用的页面、静态资源和数据库
+-- website_sample/           # 网页模板样例
+-- docs/                     # 项目文档
+-- requirements.txt          # Python 依赖列表
+-- .gitignore                # 本地缓存和环境文件忽略规则
```

更详细的目录说明见 [docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md)。

## 环境要求

建议使用 Python 3.10 或更高版本。

主要依赖记录在 `requirements.txt`：

```text
beautifulsoup4
flask
pyecharts
xlrd
xlwt
```

安装依赖：

```bash
pip install -r requirements.txt
```

## 快速开始

运行完整流程：

```bash
python app.py
```

执行后会依次完成：

1. 爬取豆瓣电影 Top250 数据
2. 写入 `website/movie.db`
3. 生成 `website/score_scatter.html`
4. 生成 `website/wordcloud.html`
5. 启动 Flask 服务

默认访问地址：

```text
http://127.0.0.1:5000
```

可访问页面：

- `/` 或 `/index`：首页
- `/movie`：电影数据分页列表
- `/score`：评分分布页面
- `/word`：词云页面

更多运行细节见 [docs/USAGE.md](docs/USAGE.md)。

## 常用脚本

| 文件 | 作用 |
| --- | --- |
| `app.py` | 项目主入口 |
| `analyze_save.py` | 爬取电影 Top250 并保存到 SQLite |
| `scatter_diagram.py` | 从数据库读取评分数据并生成散点图 |
| `cloud.py` | 从数据库读取电影名称并生成词云 |
| `web.py` | 启动 Flask 可视化网站 |
| `python/Main/movie_re（Excel）.py` | 电影 Top250 保存为 Excel 的示例 |
| `python/Main/music_soup（Excel）.py` | 音乐 Top250 保存为 Excel 的示例 |
| `python/Main/music_soup（DB）.py` | 音乐数据保存到数据库的示例 |

## 注意事项

- 豆瓣页面结构或访问策略变化时，爬虫解析规则可能需要同步调整。
- 运行爬虫时请控制访问频率，遵守目标网站的 robots、服务条款和相关法律法规。
- 当前项目偏课程实践用途，代码中保留了多个阶段的实验文件和示例模板。
- `.gitignore` 已忽略 Python 缓存、虚拟环境、本地编辑器配置和常见系统文件。
- 如果网页显示乱码，优先确认 Python 文件、HTML 文件和数据库内容是否统一使用 UTF-8 编码。

## 文档

- [运行说明](docs/USAGE.md)
- [项目结构说明](docs/PROJECT_STRUCTURE.md)
