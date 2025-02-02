import json

string_as_json = '{"name": "John Smith","age": 37}'

object = json.loads(string_as_json)


key = "name"

if key in object:
    print(object[key])
else:
    print(f'ключа >> {key} << нет')