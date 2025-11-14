import requests
import json

def fetchUserActivity(username):
    headers = {
        'Accept': 'application/vnd.github+json',
        'X-Github-Api-Version': '2022-11-28',
    }

    response = requests.get(f'https://api.github.com/users/{username}/events', headers=headers)
    data = response.text
    data_str = json.loads(data)

    print(json.dumps(data_str, indent=4))