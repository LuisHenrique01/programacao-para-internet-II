import requests
import json

url = 'https://jsonplaceholder.typicode.com/'

# GET
response = requests.get(url=url+'posts')
json_response = json.loads(response.text)

print(json.dumps(json_response,  indent=4))

# POST
data = {'title': 'Teste',
        'body': 'Este é apenas um teste',
        'userId': 1}

response = requests.post(url=url+'posts', data=data)

print(response.text, '\n Status code:', response.status_code)

# PUT
data = {'id': 1,
        'title': 'Teste de update',
        'body': 'Este é apenas um teste de update',
        'userId': 1}

response = requests.put(url=url+'posts/1', data=data)

print(response.text, '\n Status code:', response.status_code)

# PATCH
data = {'title': 'Teste de update'}

response = requests.patch(url=url+'posts/1', data=data)

print(response.text, '\n Status code:', response.status_code)

# DELETE
response = requests.delete(url=url+'posts/1')

print(response.text, '\n Status code:', response.status_code)
