import requests

url = "http://google.com"
res = requests.get(url)
print(res.text)

print(requests.__version__)
