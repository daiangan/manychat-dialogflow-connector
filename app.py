from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def connector():
    if request.method == 'POST':
        pass

    else:
        return 'I am alive!'


if __name__ == '__main__':
    app.run()
