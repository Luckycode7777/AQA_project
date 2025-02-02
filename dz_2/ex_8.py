import requests


res = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

print(res.text)