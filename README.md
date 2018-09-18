# flask_web
web框架

2018年9月17日：
session & cookie 原理

继承字典

PS:配置文件和全局变量大写

`详细内容：`

1、介绍flash  django tornado
    Django: 配置丰富
    Flask: 短小精悍
    Tornado: 异步非阻塞框架
    bottle:
    web.py:
    
2、flask 快速入门
    a 安装
        建议使用虚拟环境，避免干扰
    b wsgi, werkzenug 本质 是 soceket
    c flask
    d 应用
        示例
        装饰器： 用户认证
        多个装饰器
        反向查找的名称不允许重复
    

3、配置文件
    flask_test02.py
    
4、路由系统
    路由 + 正则表达式  flask_test03.py
    
5、模板系统

6、请求 &  响应

7、session & cookies
    flask_test05.py
    
8、闪现
    应用 对于临时数据的处理，如错误信息(s7 day140 s2.py s3.py)
9、蓝图
    用于N个应用程序的大型应用程序，每个蓝图有自己的设置
    蓝图名称 account = Blueprint('account', __name__) 和 视图函数不要重复，可以在account前面 ＋ blue

10、请求拓展 s4.py
    a.基于before_request做用户登录认证
    b.错误信息定制
    c.模板定制
        @app.template_global()
        def sb(a1, a2):
            return a1 + a2
        使用 {{ sb(1,2)}}  
    d. @app.before_first_request()
      

11、中间件
    请求的入口
12、上下文管理
    - ThreadLocal
    - 源码(request)
    http://www.cnblogs.com/wupeiqi/articles/8202353.html
    本地线程，保证即使是多个线程，自己的值也是互相隔离
        - 情况一：单进程单线程 基于全局变量做
        - 情况二：单进程多线程 threading.loacl对象
        - 情况三：单进程单线程(多个协程)， threading.local 对象做不到
     - 决定：
        - 以后不支持携程，threading.local对象
        - 支持： 自定义类似threading.local对象(支持携程)
        
        
    
    
