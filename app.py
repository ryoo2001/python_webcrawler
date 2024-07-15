from analyze_save import first_spider, db
from scatter_diagram import create_scatter_plot
from cloud import create_word_cloud
from web import run_web

def main():
    # 开始爬取提示
    first_spider()
    
    # 爬取数据并存储到数据库
    db()

    # 生成散点图和词云图
    create_scatter_plot()
    create_word_cloud()

    # 启动Flask网站服务
    run_web()

if __name__ == "__main__":
    main()
