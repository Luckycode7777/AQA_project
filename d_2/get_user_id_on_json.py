import requests

date = {
    "email": "vinkotov@example.com",
    "password": "1234"
}
res = requests.post("https://playground.learnqa.ru/api/user/login", data=date)
print(res.json())


