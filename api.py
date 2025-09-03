from snailapi import SnailApi

app = SnailApi()

@app.get("/home")
def user():
    return [b"maki chutt"]

@app.post("/user") 
def fuck():
    return [b"<h1>hello heading</h1><br><br><a href='/'>click</a>"]
