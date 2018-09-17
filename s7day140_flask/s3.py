from flask import Flask, flash, get_flashed_messages, request, redirect

app = Flask(__name__)
app.secret_key = "simzhang"

@app.route('/index')
def index():
    val = request.args.get('v')
    if val == 'oldboy':
        return 'hello world'
    flash('time out error', category='x1')
    return redirect('/error')

@app.route('/error')
def error():
    data = get_flashed_messages(category_filter=['x1'])
    msg = data[0]
    return "error message: %s " %(msg,)