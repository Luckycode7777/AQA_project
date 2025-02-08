from json.decoder import JSONDecodeError
import requests

response = requests.get("https://api.chucknorris.io/jokes/random")

url = 'https://api.chucknorris.io/jokes/random'
print(url)
print(f'response.text >>> {response.text}')


try:
    parsed_response_text = response.json() # если первая строка отработает ок, переходим к 2й, если ошибка идем в блок exept
    print(f'parsed_response_text >>> {parsed_response_text}')
except JSONDecodeError:
    print("^^^ - это не JSON формат")