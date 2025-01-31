import requests

response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param_1": "value_1"})
print(response)
print(response.text)

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param_1": "value_1"})
print(response)
print(response.text)

