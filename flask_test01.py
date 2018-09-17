from flask import Flask, render_template, request,redirect, session, url_for
app = Flask(__name__)
USERS = {
    1:{'name':'sim', 'age':'19', 'gender':'mal', 'text':'Flask 是非常灵活的，不需要使用任何特定的项目或者代码布局。但是对于初学者， 使用结构化的方法是有益无害的，亦即本教程会有一点样板的意思。'},
    2:{'name':'fei', 'age':'19', 'gender':'fel', 'text':'HSET testuser001 group AUTH_USER'}
}
# 用装饰器做重定向
def wrapper(func):
    def inner(*args, **kwargs):
        user = session.get('user_info')
        if not user:
            return redirect('/login')
        return func(*args, **kwargs)
    return inner

app.debug = True
app.secret_key = 'asas'
@app.route('/detail/<int:nid>', methods=['GET'])
def detail(nid):
    user = session.get('user_info')
    if not user:
        return  redirect('/login')
    info = USERS.get(nid)
    return render_template('detail.html', info=info)

@app.route('/index', methods=["GET"])
def index():
    user = session.get('user_info')
    if not user:
        url = url_for('l1')
        return redirect(url)
    return render_template('index.html', user_dict=USERS)

@app.route('/login', methods=['GET', 'POST'], endpoint= 'l1')
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'sim' and pwd == '123':
            session['user_info'] = user
            # return redirect('http://www.baidu.com')
        return render_template('login.html', error='id or passwd error')

if __name__ == '__main__':
    app.run