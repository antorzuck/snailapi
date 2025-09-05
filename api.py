from snailapi import SnailApi


app = SnailApi()

@app.get("/home")
def user(req, res):
    
    return res.send({
    "method":req.method,
    "q" : req.GET.get('q')
    })

