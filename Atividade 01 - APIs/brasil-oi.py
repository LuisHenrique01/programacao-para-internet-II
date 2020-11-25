import requests
import json

headers = {'Authorization': 'Token 4b88f2033fe8a200d6161b5bb87156651240897f'}
url = 'https://api.brasil.io/v1/dataset/covid19/caso/data/'
filtros = '?state=PI&date=2020-11-24'

response = requests.get(url=url+filtros, headers=headers)
json_response = json.loads(response.text)

print(json.dumps(json_response,  indent=4))
