import requests


res = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=301)

first_redirect = res.history[0]
second_redirect = res

print(res.status_code)
print(first_redirect.url)
print('---' * 5)
print(second_redirect.url)