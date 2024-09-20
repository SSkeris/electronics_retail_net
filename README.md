# "Сеть по продаже электроники"

____

### Описание задачи:

* Создать веб-приложение с API-интерфейсом и админ-панелью с кастомными действиями и фильтром по названию города через API запросы.
* Создайте базу данных, используя миграции Django.
____

### Стек:

* Python 3.8+
* Django 3+
* DRF 3.10+
* PostgreSQL 10+

____
Для запуска проекта у себя локально необходимо:

1. git clone репозитория

```
https://github.com/SSkeris/electronics_retail_net.git
```

2. Установить виртуальное окружение venv

```
python3 -m venv venv для MacOS и Linux систем
python -m venv venv для windows
```

3. Активировать виртуальное окружение

```
source venv/bin/activate для MasOs и Linux систем
venv\Scripts\activate.bat для windows
```

4. установить файл с зависимостями

```
pip install -r requirements.txt
```

5. Создать базу данных в PgAdmin, либо через терминал.
6. Заполнить своими данными файл .env в корне вашего проекта. Образец файла лежит в корне .env.sample
7. Для запуска проекта использовать команду

```
python manage.py ruserver
```
____