import requests


"""code 200"""
response = requests.get("https://playground.learnqa.ru/api/check_type", params={"nick": "Lucky", "name": "Max"})

print(response.status_code)
print(response.text)
print('***' * 10)

"""code 404"""
response = requests.get("https://playground.learnqa.ru/api/check_type$$$")

print(response.status_code)
print(response.text)
print('***' * 10)

"""code 500"""
response = requests.get("https://playground.learnqa.ru/api/get_500")

print(response.status_code)
print(response.text)
print('***' * 10)


"""code 301"""
response = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_res = response.history[0]
second_res = response

print(response.status_code)
# print(response.text)
print(first_res.url)
print("----" * 10)
print(second_res.url)
# print(response.history)
