# XLSX_parser

### Описание 
XLSX_parser - это парсер, собирает данные из xlsx-фала сотрудников компании и передает их с помощью в базу данных.

### Как запустить проект

Скачать проект с git

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```
для Windows
```
source venv/Scripts/activate
```
для Mac
```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip3 install -r requirements.txt
```

Перейти в папку /city_employment/:

```
cd city_employment
```

Выполнить миграции

```
python manage.py makemigrations
```
```
python manage.py migrate
```

Создать суперпользователя

```
python3 manage.py createsuperuser
```

Адрес админ-панели - http://127.0.0.1:8000/admin

Запустить локальный сервер

```
python manage.py runserver
```

Перейти по адресу - http://127.0.0.1:8000


- Нажать на кнопку "выбрать файл", выбрать необхожимый файл для парсинга
- Нажать на кнопку "загрузить файл"

Данные вашего файла через определенное количество времени загрузится в базу данных.

### Стек технологий:
- Python 3.7
- Django 2.2.16
- PostgreeSQL
- Openpyxl

### Авторы проекта
Михаил Брагин
