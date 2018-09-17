from flask import Flask, flash, get_flashed_messages,request,redirect
app = Flask(__name__)
app.secret_key = 'simzhangbest'
@app.route('/get')
def get():
    # 从某个地方获取设置过的所有值，并清除
    data = get_flashed_messages()
    print(data)

@app.route('/set')
def set():
    # 向某一个地方设置值
    flash("simzhangbest's flash")

if __name__ == '__main__':
    app.run()