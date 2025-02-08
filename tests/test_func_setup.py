import requests
import pytest

from lib.base_case import BaseCase


class TestUserAuth2(BaseCase):
    exclude_params = [
        ('no_cookie'),
        ('no_token')
    ]

    def setup(self):
        date = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        url_user_login = "https://playground.learnqa.ru/api/user/login"
        response_1 = requests.post(url_user_login, data=date)

        self.auth_sid = self.get_cookie(response_1, "auth_sid")
        self.token = self.get_header(response_1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response_1, "user_id")

        # assert "user_id" in response_1.json(), 'Это не тот юзер ай ди'
        # self.user_id_from_auth_method = response_1.json()["user_id"]

    def test_auth_user(self):
        response_2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        assert "user_id" in response_2.json(), "Что это?"

        user_id_from_check_method = response_2.json()["user_id"]
        print(user_id_from_check_method)

        assert self.user_id_from_auth_method == user_id_from_check_method, "Не равны"

    @pytest.mark.parametrize('conditionz', exclude_params)
    def test_negative_auth_check(self, conditionz):

        if conditionz == 'no_cookie':
            response_2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token": self.token}
            )
        else:
            response_2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={"auth_sid": self.auth_sid}
            )

        assert 'user_id' in self.response_1.json(), 'Это не тот user id'

        user_id_from_check_method = response_2.json()["user_id"]

        assert user_id_from_check_method == 0, f'Юзер авторизован с каким-то из параметров >>> {conditionz}'

