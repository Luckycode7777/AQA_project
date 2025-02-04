import requests


class TestUserAuth:
    def test_user_auth(self):
        date = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        url_user_login = "https://playground.learnqa.ru/api/user/login"
        response_1 = requests.post(url_user_login, data=date)

        assert "auth_sid" in response_1.cookies, 'Это не куки'
        assert "x-csrf-token" in response_1.headers, 'Это неверный токен'
        assert "user_id" in response_1.json(), 'Это не тот юзер ай ди'

        auth_sid = response_1.cookies.get("auth_sid")
        token = response_1.headers.get("x-csrf-token")
        user_id_from_auth_method = response_1.json()["user_id"]

        response_2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        assert "user_id" in response_2.json(), "Что это?"

        user_id_from_check_method = response_2.json()["user_id"]

        assert user_id_from_auth_method == user_id_from_check_method, "Не равны"







