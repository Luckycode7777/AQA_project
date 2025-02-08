import requests

date = {
    "email": "vinkotov@example.com",
    "password": "1234"
}
res = requests.post("https://playground.learnqa.ru/api/user/login", data=date)
print(res.text)
print(dict(res.json()))
print(res.headers)
print(dict(res.cookies))

assert 'auth_sid' in res.cookies, 'куки не получил'
assert 'x-csrf-token' in res.headers, 'такого нет'
assert 'user_id' in res.json(), 'не тот user_id'

print('*' * 15)
print(res.cookies.get('auth_sid'))
print(res.headers.get('x-csrf-token'))
print(res.json()['user_id'])

