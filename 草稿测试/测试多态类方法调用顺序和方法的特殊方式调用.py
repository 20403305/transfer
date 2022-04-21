



class QueryModelMixin:
    def get(self):
        handle_set = 'list'
        handle = getattr(self, handle_set)
        return handle()


class anotherclass():
    def __init__(self) -> None:
        self.pk = 123

    def query(self):
        print("anotherclass")


class anotherclass_a():
    def __init__(self) -> None:
        self.pk = 123

    def query(self):
        print("anotherclass_a")

class ListModelMixin(QueryModelMixin,anotherclass_a,anotherclass,):

    def list(self):
        print("1111111111")
        self.query()

def abc():
    var = ListModelMixin()

    a = var.get()

abc()
