import json
import requests


url = 'https://playground.learnqa.ru/api/user/login'
data = {
    "email": "vinkotov@example.com",
    "password": "1234"
}

res = requests.post(url, data=data)
print(dict(res.json()))
