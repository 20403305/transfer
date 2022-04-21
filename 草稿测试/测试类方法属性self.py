
import functools


def check_scheme(cls):
    def _check_scheme(func):
        @functools.wraps(func)
        def wraps(*args, **kwargs):
            cls.pre_view(func.__name__, kwargs['self'])
            try:
                res = func(*args, **kwargs)
            except Exception:
                raise
            finally:
                print("finally")
            return res
        return wraps
    return _check_scheme

class BasicView:
    @classmethod
    async def pre_view(cls, func_name, _self):
        cls.action = func_name
        print(_self)

    @classmethod
    def as_view(cls, name):
        func = check_scheme(cls)(getattr(cls, name))
        func(kwargs="123",self=cls)

class AgencyHandle(
    BasicView
):
    def post(self,kwargs):
        print("sdf")
        print(kwargs)

    def say_hello(self):
        print("hello")

AgencyHandle.as_view("post")
