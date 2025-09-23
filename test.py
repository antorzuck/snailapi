import requests as r

xx = r.get('http://127.0.0.1:8000/home')


print(xx.text)
