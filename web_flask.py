import flask
from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__, static_url_path='', static_folder='website',
                  template_folder='website')

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route('/movie')
def movie():
    page = request.args.get('page', 1, type=int)
    per_page = 25
    offset = (page - 1) * per_page

    conn = sqlite3.connect('movie.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM movie')
    total_movies = cursor.fetchone()[0]
    total_pages = (total_movies + per_page - 1) // per_page

    cursor.execute('SELECT * FROM movie LIMIT ? OFFSET ?', (per_page, offset))
    movies = cursor.fetchall()
    conn.close()

    return render_template('movie.html', movies=movies, page=page, total_pages=total_pages)

if __name__ == '__main__':
 app.run(host='127.0.0.1', port=5000)