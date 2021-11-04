import requests

with open('token.txt', 'r') as token_file:
    token = token_file.readline()


def shorten_link(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    shortener_url = 'https://api-ssl.bitly.com/v4/shorten'
    json = {
        'long_url': url
    }
    response = requests.post(shortener_url, json=json, headers=headers)

    response.raise_for_status()
    return response.json()['id']


link_to_shorten = input('Input link to short: ')
try:
    bitlink = shorten_link(token, link_to_shorten)
except requests.exceptions.HTTPError:
    print('Что-то пошло не так')
else:
    print(bitlink)
