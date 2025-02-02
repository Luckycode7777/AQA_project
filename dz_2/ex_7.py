import requests


res = requests.get("https://playground.learnqa.ru/api/compare_query_type", params="get")

print(res.text)