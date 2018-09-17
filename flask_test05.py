from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'simzhangbest'
@app.route('/')
def index():
    session['k1'] = 'v1'
    session['k2'] = 'v2'

    return "xx"


if __name__ == '__main__':
    app.run()