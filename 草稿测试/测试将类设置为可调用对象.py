

def test():
    print("test")

class decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('call %s():' % self.func.__name__)
        return self.func(*args, **kwargs)

a = decorator(test)
a()
