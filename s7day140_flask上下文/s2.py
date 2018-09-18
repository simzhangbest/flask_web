import threading
from _thread import get_ident
class Local(object):
    def __init__(self):
        self.storage = {}
        self.get_ident = get_ident

    def set(self, k, v):
        indent = self.get_ident()
        self.storage.get

def task(arg):
    v = get_ident()
    print(v)

for i in range(20):
    th = threading.Thread(target=task, args=(i,))
    th.start()