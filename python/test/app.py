import flask
import sqlite3

app = flask.Flask(__name__, static_url_path='', static_folder='./website',
                  template_folder='./website')

@app.route("/")
def index():
    return flask.render_template("douban.html")


@app.route("/index")
def douban():
    return flask.render_template("douban.html")


@app.route("/movie")
def movie():
    datalist = []
    con = sqlite3.connect('music.db')
    cur = con.cursor()
    sql = "select * from movie_top250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return flask.render_template("movie.html", movies=datalist)


@app.route("/score")
def score():
    score = []  # 评分
    number = []  # 每个评分对应的电影数量
    conn = sqlite3.connect("music.db")
    cur = conn.cursor()
    sql = "select score,count(score) from movie_top250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        number.append(item[1])

    cur.close()
    conn.close()
    return flask.render_template('score.html', score=score, number=number)


@app.route("/word")
def word():
    return flask.render_template("word.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

