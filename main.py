import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def is_bitlink(url):
    return urlparse(url).netloc == 'bit.ly'


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
    cleared_link = f'{parsed_link.netloc}{parsed_link.path}'

    counter_url = f'https://api-ssl.bitly.com/v4/bitlinks/{cleared_link}/clicks/summary'
    response = requests.get(counter_url, headers=headers)

    response.raise_for_status()
    return response.json()['total_clicks']


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')
    user_link = input('Введите ссылку: ')
    try:
        if is_bitlink(user_link):
            print(f'Количество кликов по ссылке: {count_clicks(token, user_link)}')
        else:
            print(f'Битлинк: {shorten_link(token, user_link)}')
    except requests.exceptions.HTTPError:
        print('Что-то пошло не так')
