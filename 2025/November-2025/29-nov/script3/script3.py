import requests

url = "https://httpbin.org/image/png"

res = requests.get(url)

with open("download.png","wb")as file:
    file.write(res.content)

print("Image downloaded and saved as downloaded.png")