import requests

headers = {
    'Accept': 'application/vnd.github+json',
    'X-Github-Api-Version': '2022-11-28',
}

response = requests.get('https://api.github.com/users/JoaoGRSilva/events', headers=headers)

print(response.text)