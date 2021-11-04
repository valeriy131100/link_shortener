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
    if response.ok:
        return response.json()['id']
    else:
        return None


link_to_shorten = input('Input link to short: ')
print('Битлинк', shorten_link(token, link_to_shorten))
