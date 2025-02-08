import json.decoder

from requests import Response

class BaseCase:
    def get_cookie(self, response: Response, coolie_name):
        assert coolie_name in response.cookies, f'Не может найти куки с именем {coolie_name} в последнем ответе'
        return response.cookies[coolie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f'Нет хедеров с именем {headers_name} в посл ответе'
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Ответ не в JSON формате. Ответ в тексте "{response.text}"'

        assert name in response_as_dict, f'Ответ JSON не имеет ключа "{name}"'

        return response_as_dict[name]