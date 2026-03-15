import requests

info = {"username":"istiak","role":"devops"}
url = "https://httpbin.org/post"

res = requests.post(url, json=info)

print(res.json()["json"])