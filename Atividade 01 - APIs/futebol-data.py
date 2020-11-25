import requests
import json

headers = {'X-Auth-Token': '83b15ff65908477d81aa9416f07a7667'}
url = 'https://api.football-data.org/v2/matches'

response = requests.get(url=url, headers=headers)
json_response = json.loads(response.text)

print(json.dumps(json_response,  indent=4))
