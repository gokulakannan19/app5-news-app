import requests
from send_email import send_email

url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-11-30&sortBy=publishedAt&apiKey=")

request = requests.get(url)
content = request.json()

raw_message = ""
for article in content["articles"]:
    article_message = f"{article['title']} \n {article['description']} \n\n"
    raw_message = raw_message + article_message

message = f"""\
Subject: Daily News

{raw_message}
"""

message = message.encode("utf-8")

send_email(message)
print(content)