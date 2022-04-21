# 创建一个装饰器类
class Decorator:
    def __init__(self, func):
        self.name = func.__name__
        self.func = func

    def __call__(self, *args, **kwargs):
        print("before")
        self.func(self,*args, **kwargs)
        print("after")
    
    def __str__(self):
        return self.name
    
    # def __repr__(self):
    #     return self.name
    
    # def __getattr__(self, item):
    #     return getattr(self.func, item)
    
    # def __getattribute__(self, item):
    #     return getattr(self.func, item)
    
    # def __get__(self, instance, owner):
    #     return self.func.__get__(instance, owner)
    
    # def __set__(self, instance, value):
    #     self.func.__set__(instance, value)
        
    # def __delete__(self, instance):
    #     self.func.__delete__(instance)
        
    # def __set_name__(self, owner, name):
    #     self.name = name
    #     self.func.__set_name__(owner, name)
    
    def update_name(self, name):
        self.name = name
        self.func.__name__ = name
        print("update_name")

@Decorator
def test(self,age,address):
    print(self.update_name("good"))

test(5,'hotel')
