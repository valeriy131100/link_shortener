import requests
from urllib.parse import urlparse


def get_token_from_file():
    with open('token.txt', 'r') as token_file:
        return token_file.readline()


def is_bitlink(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc == 'bit.ly':
        return True
    else:
        return False


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


def count_clicks(token, link):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    parsed_link = urlparse(link)
    cleared_link = parsed_link.netloc + parsed_link.path

    counter_url = f'https://api-ssl.bitly.com/v4/bitlinks/{cleared_link}/clicks/summary'
    response = requests.get(counter_url, headers=headers)

    response.raise_for_status()
    return response.json()['total_clicks']


if __name__ == '__main__':
    try:
        token = get_token_from_file()
    except FileNotFoundError:
        print('Не найден файл токена. Пожалуйста, положите его в файл token.txt в директории программы')
    else:
        user_link = input('Введите ссылку: ')
        if is_bitlink(user_link):
            try:
                click_count = count_clicks(token, user_link)
            except requests.exceptions.HTTPError:
                print('Что-то пошло не так')
            else:
                print('Количество кликов по ссылке:', click_count)
        else:
            try:
                bitlink = count_clicks(token, user_link)
            except requests.exceptions.HTTPError:
                print('Что-то пошло не так')
            else:
                print('Битлинк:', bitlink)
