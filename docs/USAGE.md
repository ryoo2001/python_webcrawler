# 运行说明

本文档说明 `python_webcrawler` 的本地运行方式、输出文件和常见问题。

## 1. 准备环境

建议使用虚拟环境隔离依赖：

```bash
python -m venv .venv
```

Windows PowerShell：

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS / Linux：

```bash
source .venv/bin/activate
```

安装依赖：

```bash
pip install beautifulsoup4 flask pyecharts xlrd xlwt
```

## 2. 运行完整项目

在项目根目录执行：

```bash
python app.py
```

程序会执行完整流程：

```text
爬取豆瓣电影 Top250
  -> 保存到 website/movie.db
  -> 生成评分散点图
  -> 生成电影词云
  -> 启动 Flask 网站
```

启动成功后访问：

```text
http://127.0.0.1:5000
```

## 3. 页面路由

| 路由 | 说明 |
| --- | --- |
| `/` | 首页 |
| `/index` | 首页 |
| `/movie` | 电影列表，支持分页 |
| `/movie?page=2` | 第 2 页电影列表 |
| `/score` | 评分分布页面 |
| `/word` | 词云页面 |

## 4. 输出文件

| 文件 | 来源 | 说明 |
| --- | --- | --- |
| `website/movie.db` | `analyze_save.py` | SQLite 数据库，保存电影 Top250 |
| `website/score_scatter.html` | `scatter_diagram.py` | pyecharts 评分分布图 |
| `website/wordcloud.html` | `cloud.py` | pyecharts 词云图 |
| `豆瓣电影top250.xls` | `python/Main/movie_re（Excel）.py` | 电影 Excel 导出示例 |
| `豆瓣音乐top250.xls` | `python/Main/music_soup（Excel）.py` | 音乐 Excel 导出示例 |

## 5. 单独运行示例脚本

电影数据保存为 Excel：

```bash
python "python/Main/movie_re（Excel）.py"
```

音乐数据保存为 Excel：

```bash
python "python/Main/music_soup（Excel）.py"
```

只启动 Flask 网站：

```bash
python web.py
```

注意：`web.py` 中只定义了 `run_web()`，如果要直接运行该文件，需要在文件末尾补充调用逻辑，或通过 `app.py` 启动。

## 6. 常见问题

### 爬取失败或没有数据

可能原因：

- 网络无法访问豆瓣页面
- 豆瓣页面结构发生变化
- 请求过于频繁，被目标网站限制
- User-Agent 或请求头需要调整

建议先在浏览器打开目标页面确认是否能正常访问，再检查 `analyze_save.py` 中的解析规则。

### 页面没有图表

确认以下文件是否已经生成：

```text
website/score_scatter.html
website/wordcloud.html
```

如果不存在，先运行：

```bash
python app.py
```

### 数据重复

`analyze_save.py` 当前会向已有 `website/movie.db` 继续插入数据。如果多次运行完整流程，可能出现重复记录。需要重新生成数据时，可以先备份并删除旧的 `website/movie.db`。

### 中文乱码

项目中部分历史文件可能存在编码不一致问题。建议统一使用 UTF-8 保存 Python、HTML 和 Markdown 文件。

## 7. 合规提示

本项目用于 Python 爬虫、数据处理和可视化课程实践。运行爬虫时请控制访问频率，不要对目标网站造成压力，并遵守目标网站的 robots、服务条款和相关法律法规。
