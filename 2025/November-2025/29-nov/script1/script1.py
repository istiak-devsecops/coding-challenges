import requests

info = {"name":"istiak","role":"devops"}
head = {"User-Agent": "MyPythonScript/1.0", "X-Custom-Header": "Istiak-Test"}

res = requests.get("https://httpbin.org/get", params=info, headers=head)

data = res.json()

print(f"Url: {res.url}")
print(f"{data["headers"]}")