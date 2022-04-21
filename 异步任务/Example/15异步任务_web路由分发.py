from aiohttp import web

# 如果需要使用装饰器来路由url的话，需要创建RouteTableDef类的对象来获取一个装饰器

routes = web.RouteTableDef()

@routes.get('/get')
async def get_req(request):
    print("this is get request")
    return web.Response(text="Hello World")

@routes.post('/post')
async def post_req(request):
    print("this is post request")
    return web.Response(text="Post Success")

@routes.route("*","/all")#支持GET/POST/PUT/DELETE等请求方式
async def all_handler(request):
    print("this is all request")
    print(request.method)
    print(type(request))
    print("handle all request")
    return web.Response(text="All Success")

def main():
    pass

if __name__ == '__main__':
    app = web.Application()
    # 如果不适用装饰器的话，添加如下代码
    # app.router.add_route([web.get('/get', get_req), web.post('/post', post_req), web.route("*", "/all", all_handler)])
    # 如果使用装饰器的话，添加如下代码
    app.add_routes(routes)
    web.run_app(app)
