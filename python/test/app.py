from flask import Flask

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

# @app.route("/user")
# def welcome():
#     return "Hello"

# @app.route("/user/<name>")
# def welcome_user(name):
#     return f"欢迎用户{name}!"


if __name__ == '__main__':
    app.run(host='localhost', port=5000)