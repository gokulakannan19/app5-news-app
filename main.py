import requests
from send_email import send_email

topic = "tesla"
API_KEY = "####"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2024-11-30&"
       "sortBy=publishedAt&"
       f"apiKey={API_KEY}&"
       "language=en")

request = requests.get(url)
content = request.json()

raw_message = ""
for article in content["articles"][:10]:
    article_message = f"{article['title']} \n{article['description']} \n{article['url']} \n\n"
    raw_message = raw_message + article_message

message = f"""\
Subject: Daily News

{raw_message}

Thanks,
goks
"""

message = message.encode("utf-8")
send_email(message)
print("Done")