# 模板
from flask import Flask, render_template, Markup, jsonify,session
app = Flask(__name__)
app.config.from_object("settings.ProductionConfig")

def func1(arg):
    return Markup("<input type = 'text' value = '%s' />" %(arg,))

@app.route('/')
def index():
    return render_template('index_sim1.html', ff = func1)

if __name__ == '__main__':
    app.run()