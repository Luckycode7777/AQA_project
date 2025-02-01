import requests

"""Получаем куки"""
payload = {"login": "secret_login", "password": "secret_passZ"}  # готовим данные
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
print(response1.headers)
print(dict(response1.cookies))

cookie_value = response1.cookies.get('auth_cookie') # получаем название auth_cookie и кладем в эту переменную
print(cookie_value)

print('*****' * 5)


"""Применяем полученные куки"""
cookies = {}
if cookie_value is not None:
    cookies = {'auth_cookie': cookie_value}  # создали словарь для авторизованной куки
print(cookies)

response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)  # сделали запрос

print(response2.text)