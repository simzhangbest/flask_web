from flask import Flask, render_template, request,redirect
app = Flask(__name__)

@app.route('/login', methods=['GET'])
def index():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'sim' and pwd == '123':
            return redirect('http://www.baidu.com')
        return render_template('login.html', error='id or passwd error')

if __name__ == '__main__':
    app.run