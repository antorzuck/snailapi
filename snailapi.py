class SnailApi:

    def __init__(self):
        self.routes = dict()
        print(self.routes)


    def __call__(self, environ, start_response):
        path = environ["PATH_INFO"]
        query = environ.get("QUERY_STRING", "")
        
        req_method = environ.get('REQUEST_METHOD')
        

        handler = self.routes.get(path)
        if req_method in handler:
            print(handler)
            start_response("200 OK", [('Content-Type','Text/HTML')])


            return handler[req_method]()
        else:
            start_response("200 OK", [('Content-Type','Text/Plain')])
            return [b"method not allowed bro or the route dont exist!"]
            
            
            
    def add_to_route(self, path, method, handler):
        if path not in self.routes:
            self.routes[path] = {}
        self.routes[path][method] = handler
        
        print(self.routes)
        
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


