import flask
from flask import Flask, render_template, request
import sqlite3

def run_web():
    app = Flask(__name__, static_url_path='', static_folder='website',
                  template_folder='website')

    @app.route("/")
    def index():
        return flask.render_template("index.html")

    @app.route("/index")
    def index1():
        return flask.render_template("index.html")

    @app.route('/movie')
    def movie():
        page = request.args.get('page', 1, type=int) # 请求参数中获取当前页码。如果没有提供页码参数，默认值为1
        per_page = 25 # 设置每页显示的记录数
        offset = (page - 1) * per_page # 根据当前页码计算查询数据库时的偏移量，用于跳过前面已经访问过的页面
 
        # 连接数据库并获取总记录数
        conn = sqlite3.connect('website/movie.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM movie')
        total_movies = cursor.fetchone()[0]
        total_pages = (total_movies + per_page - 1) // per_page # 根据总记录数和每页显示的记录数计算总页数

        # 从数据库中查询当前页需要显示的记录，使用LIMIT(数据范围)和OFFSET(跳过的数据)实现分页查询
        cursor.execute('SELECT * FROM movie LIMIT ? OFFSET ?', (per_page, offset))
        movies = cursor.fetchall()
        conn.close()

        return render_template('movie.html', movies=movies, page=page, total_pages=total_pages) # 将查询到的记录、当前页码和总页数传递给模板文件

    @app.route("/score")
    def score():
        return flask.render_template('score.html')

    @app.route("/word")
    def word():
        return flask.render_template("word.html")


    app.run(host='127.0.0.1', port=5000)


