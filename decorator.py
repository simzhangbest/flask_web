# 装饰器
url_map = {
 'index': index
}

def route(option):
    def inner(func, *args, **kwargs):
        url_map[option['path']] = func
    return inner

@route({'path':'/index'})
def index(request):
    pass