from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from us to them!'


if __name__ == '__main__':
    app.run()
