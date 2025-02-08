import pytest
import requests


class TestFirstAPI:
    names = [
        ("Max"),
        ("Tonya"),
        (""),
    ]

    @pytest.mark.parametrize('n_name', names)
    def test_hello(self, n_name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {"name": n_name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, 'Неверный код ответа/Wrong response code'

        response_dict = response.json()
        assert "answer" in response_dict, "Не найдено 'answer' в ответе"

        if len(n_name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {n_name}"

        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, "Актуальный ответ не корректынй"
