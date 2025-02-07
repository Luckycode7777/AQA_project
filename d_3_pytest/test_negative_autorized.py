import pytest
import json

import requests


class TestUserAuthNegative:
    exclude_params = [
        ('no_cookie'),
        ('no_token')
    ]

    @pytest.mark.parametrize('conditionz', exclude_params)
    def test_negative_auth_check(self, conditionz):
        date = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        url_user_login = "https://playground.learnqa.ru/api/user/login"
        response_1 = requests.post(url_user_login, data=date)

        assert "auth_sid" in response_1.cookies, 'Это не куки'
        assert "x-csrf-token" in response_1.headers, 'Это неверный токен'

        auth_sid = response_1.cookies.get("auth_sid")
        token = response_1.headers.get("x-csrf-token")

        if conditionz == 'no_cookie':
            response_2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token": token}
            )
        else:
            response_2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={"auth_sid": auth_sid}
            )

        assert 'user_id' in response_1.json(), 'Это не тот user id'

        user_id_from_check_method = response_2.json()["user_id"]

        assert user_id_from_check_method == 0, f'Юзер авторизован с каким-то из параметров >>> {conditionz}'
