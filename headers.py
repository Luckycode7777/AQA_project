import requests

headers = {"some_header": "1234"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)

print(response.text)  # ответ сервера. заголовки которые он получил в запросе от клиента(от меня)
print('***' * 20)
print('***' * 20)
print(response.headers)  # ответ сервера на этот запрос