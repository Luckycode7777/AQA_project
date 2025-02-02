import requests

"""Получение куки"""
payload = {"login": "secret_login", "password": "secret_pass"}  # готовим данные
response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)  # передаем данные в date

# выводим параметры ответа
print(response.status_code)
# print(response.text)
print(dict(response.cookies))
print(type(response.cookies))

print("***" * 5)
print(response.headers)


# если ошибка ожидаемая и все работает в штатном режиме, код ответа будет успешным те 200

