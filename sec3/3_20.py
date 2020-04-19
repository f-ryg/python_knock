import json
jawiki = 'jawiki-country.json'

json_open = open(jawiki,'r')
for line in json_open:
    article = json.loads(line)
    if "イギリス" == article["title"]:
        print(article["text"])