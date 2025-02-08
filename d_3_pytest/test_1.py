import requests


class TestFirstAPI:
    def test_hello(self):
        url = "https://playground.learnqa.ru/api/hellos"
        name = "Max"
        data = {"name": name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, 'Неверный код ответа/Wrong response code'

        # ответ в json парсим в переменную response_dict
        response_dict = response.json()
        assert "answer" in response_dict, "Не найдено 'answer' в ответе"
        print(f'dict(response.json()) >>> {dict(response.json())}')

        expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, "Актуальный ответ не корректынй"
        print(f'actual_response_text >>> {actual_response_text}')
        print(f'expected_response_text >>> {expected_response_text}')
