import requests


request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
print(content)