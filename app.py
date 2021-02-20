from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Hello, There!!</h1>"


@app.route('/<string:name>')
def greet(name):
    # return f"Hello, {name}!!"
    greeting = f'<h1>Hello, {name}!!</h1>'
    return greeting


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
