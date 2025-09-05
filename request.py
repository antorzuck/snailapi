from urllib.parse import parse_qs

class Request:
    
    def __init__(self, environ):
    
        self.path = environ["PATH_INFO"]
        self.query = environ.get("QUERY_STRING", "")
        self.method = environ.get('REQUEST_METHOD')
        self.query_string = environ.get("QUERY_STRING", "")
        
        self.GET = {k: v[0] if len(v) == 1 else v 
                    for k, v in parse_qs(self.query_string).items()}
        
   
