# 装饰器
# url_map = {
#  'index': index
# }
#
# def route(option):
#     def inner(func, *args, **kwargs):
#         url_map[option['path']] = func
#     return inner
#
# @route({'path':'/index'})
# def index(request):
#     pass

import functools

def wrapper(func):
    @functools.wraps(func) # 帮助设置函数的元信息
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner
@wrapper
def f1():
    pass

# 使用functools 打印 f1
# 不使用functools 打印 inner
# print(f1.__name__)
