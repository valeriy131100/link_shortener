# link_shortener
Создает битлинки и выводит по ним количество кликов.

# Установка
Вам понадобится установленный Python 3.6-3.9 и git

Склонируйте репозиторий
```bash
$ git clone https://github.com/valeriy131100/link_shortener
```

Создайте в этой папке виртуальное окружение
```bash
$ python3 -m venv [полный путь до папки link_shortener]
```

Активируйте виртуальное окружение и установите зависимости
```bash
$ cd link_shortener
$ source bin/activate
$ pip install -r requirements.txt
```
# Использование
Заполните прилагающийся .env.exapmle файл и переименуйте его в .env или иным образом задайте переменную среды BITLY_TOKEN.

Находясь в директории link_shortener исполните main.py указав первым аргументом ссылку или битлинк
```bash
$ bin/python main.py [some_url_here]
```

В случае, если ссылка не является битлинком, то программа создаст его
```bash
$ bin/python main.py https://google.com
Битлинк: bit.ly/3nQjVCw
```
Если ссылка является битлинком, то по ней вернется количество кликов за все время
```bash
$ bin/python main.py https://bit.ly/3nQjVCw
Количество кликов по ссылке: 1
```
В случае если со ссылкой что-то не так, то программа сообщит  об этом
```bash
$ bin/python main.py something_that_not_url
Что-то пошло не так
```
Будте внимательны, не забудьте указывать http:// или https:// в начале ссылки


