# 处理配置文件
from flask import Flask
app = Flask(__name__)
app.config.from_object("settings.ProductionConfig")

@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run()