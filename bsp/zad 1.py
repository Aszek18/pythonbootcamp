import json

obiekt = {"imie": "Jan", "wiek":33}
print(type(json.dumps(obiekt)))

napis = '{"imie": "Jan", "wiek":[33,13]}'
print(json.loads(napis)["wiek"])