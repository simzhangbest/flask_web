# 路由系统
# 正则

from werkzeug.routing import BaseConverter
from flask import Flask, url_for

app = Flask(__name__)


class RegexConverter(BaseConverter):
    """
    自定义URL匹配正则表达式
    """

    def __init__(self, map, regex):
        super(RegexConverter, self).__init__(map)
        self.regex = regex

    def to_python(self, value):
        """
        路由匹配时，匹配成功后传递给视图函数中参数的值
        :param value:
        :return:
        """
        return int(value)

    def to_url(self, value):
        """
        使用url_for反向生成URL时，传递的参数经过该方法处理，返回的值用于生成URL中的参数
        :param value:
        :return:
        """
        val = super(RegexConverter, self).to_url(value)
        return val

# 添加到flask中
app.url_map.converters['regex'] = RegexConverter

@app.route('/index/<regex("\d+"):nid>')
def index(nid):
    print(url_for('index', nid='888'))
    return 'Index'

@app.route('/index', methods=['GET', 'POST'], endpoint='n1', redirect_to='/index2')
def index():
    return 'old'

@app.route('/index2' ,methods=['GET', 'POST'], endpoint='n2')
def index2():
    return "new"

if __name__ == '__main__':
    app.run()
