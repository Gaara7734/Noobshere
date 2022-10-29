import requests

response = requests.get("https://www.kucoin.com/_api/cms/articles?page=1&pageSize=10&category=listing&lang=en_US")

jsoncode = response.json()

options = jsoncode['items']

for i in range(len(options)):
    title = options[i]['title']
    date = options[i]['summary']
    print(f"{title} : {date}")
