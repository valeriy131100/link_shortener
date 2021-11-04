import requests

with open('token.txt', 'r') as token_file:
    token = token_file.readline()

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

shortener_url = 'https://api-ssl.bitly.com/v4/shorten'
link_to_shorten = input('Input link to short: ')

json = {
    'long_url': link_to_shorten
}

response = requests.post(shortener_url, json=json, headers=headers)

if response.ok:
    print(response.json()['id'])
else:
    print(response.status_code)
