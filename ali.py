import requests


resp = requests.get("https://www.alibaba.com")
print(resp.text)
