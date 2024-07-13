import flask
from flask import Flask, render_template


app = Flask(__name__, static_url_path='', static_folder='music_website',
                  template_folder='music_website')

@app.route("/")
def index():
    return flask.render_template("index.html")

if __name__ == '__main__':
 app.run(host='127.0.0.1', port=5000)