from json.decoder import JSONDecodeError
import requests


json_text = requests.get("https://gist.github.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37")
print(json_text.text)

try:
    parsed_json_text = json_text.json()
    print(parsed_json_text)
except JSONDecodeError:
    print('Response is not a JSON format')
