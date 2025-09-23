from response import Response
from request import Request


class SnailApi:

    def __init__(self):
        self.routes = dict()
        self.middleware = []


    def __call__(self, environ, start_response):
       
        request = Request(environ)
        response = Response()
        handler = self.routes.get(request.path)
        for mid in self.middleware:
            middleware_response = mid(request, response)
            if not middleware_response == True:
                return response.asgi(start_response)
        try:
            if request.method in handler:
                handler[request.method](request, response)
                return response.asgi(start_response)

        except Exception as e:
            start_response("200 OK", [('Content-Type','application/json')])
            return [b"method not allowed bro or the route dont exist!"]


    def add_to_route(self, path, method, handler):
        if path not in self.routes:
            self.routes[path] = {}
            
        self.routes[path][method] = handler
        return handler


    def get(self, path):
        def wrapper(handler):
            self.add_to_route(path=path, method="GET", handler=handler)
            
        return wrapper
        
    def post(self, path):
        def wrapper(handler):
            self.add_to_route(path=path, method="POST", handler=handler)
            
        return wrapper
        
    def put(self, path):
        def wrapper(handler):
            self.add_to_route(path=path, method="PUT", handler=handler)
            
        return wrapper
        
    def delete(self, path):
        def wrapper(handler):
            self.add_to_route(path=path, method="DELETE", handler=handler)
            
        return wrapper    


    def add_middleware(self, func):
        self.middleware.append(func)
        print(self.middleware)
