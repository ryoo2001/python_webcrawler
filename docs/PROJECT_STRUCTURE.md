# 项目结构说明

本文档按目录说明 `python_webcrawler` 仓库中各部分的用途，便于后续维护和课程展示。

## 根目录脚本

| 文件 | 说明 |
| --- | --- |
| `app.py` | 项目主入口，串联爬取、入库、图表生成和 Flask 启动 |
| `analyze_save.py` | 爬取豆瓣电影 Top250，并写入 `website/movie.db` |
| `scatter_diagram.py` | 查询电影评分数据，生成评分分布散点图 |
| `cloud.py` | 查询电影名称数据，生成词云图 |
| `web.py` | 定义 Flask 应用、页面路由和本地服务 |

## `website/`

Flask 实际使用的网站目录。

| 路径 | 说明 |
| --- | --- |
| `website/index.html` | 首页模板 |
| `website/movie.html` | 电影列表模板 |
| `website/score.html` | 评分图表页面 |
| `website/word.html` | 词云页面 |
| `website/movie.db` | 电影数据 SQLite 数据库 |
| `website/css/` | 页面样式资源 |
| `website/js/` | 页面脚本和 ECharts 资源 |
| `website/images/` | 页面图片和生成图片 |
| `website/fonts/` | 页面字体资源 |

## `python/Main/`

课程主线代码和爬虫示例。

| 文件或目录 | 说明 |
| --- | --- |
| `爬虫基础操作.py` | 爬虫基础练习 |
| `Flask网页搭建.py` | Flask 页面搭建练习 |
| `movie_re（Excel）.py` | 使用正则解析电影 Top250 并保存为 Excel |
| `music_soup（Excel）.py` | 使用 BeautifulSoup 解析音乐 Top250 并保存为 Excel |
| `music_soup（DB）.py` | 音乐数据入库示例 |
| `music_soup（no save）.py` | 只爬取和解析，不保存数据的示例 |
| `数据处理/` | BeautifulSoup、正则、Excel 读取等课堂练习 |

## `python/test/`

测试和实验脚本目录，主要用于验证爬虫、网页生成和数据处理逻辑。

## `temp_date/`

历史数据、实验输出和临时页面。

| 文件 | 说明 |
| --- | --- |
| `movie.db` | 电影数据历史数据库 |
| `music.db` | 音乐数据历史数据库 |
| `豆瓣电影top250.xls` | 电影 Top250 Excel 样例 |
| `Main.html` | 历史页面输出 |
| `douban_movie.html` | 电影页面实验输出 |
| `douban_music.html` | 音乐页面实验输出 |

## `website_sample/`

网站模板样例目录，保留了完整的静态资源和页面结构，作为课程展示和 `website/` 的参考版本。

## 项目配置文件

| 文件 | 说明 |
| --- | --- |
| `.gitignore` | 忽略 Python 缓存、虚拟环境、本地编辑器配置和常见系统文件 |
| `requirements.txt` | 记录项目运行所需的 Python 依赖 |

## 数据流

```text
豆瓣 Top250 页面
  -> analyze_save.py 爬取与解析
  -> website/movie.db
  -> scatter_diagram.py / cloud.py
  -> website/score_scatter.html / website/wordcloud.html
  -> web.py Flask 页面展示
```

## 维护建议

- 后续新增依赖时，建议补充 `requirements.txt`。
- 自动生成文件可以单独放入 `output/` 或 `website/generated/`，便于区分源码和运行结果。
- 数据库重复插入问题可以通过清表、唯一索引或运行前重建数据库解决。
- 如果继续扩展爬虫，建议为电影和音乐分别建立模块，减少根目录脚本数量。
