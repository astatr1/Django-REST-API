Учебный проект по загрузке файлов на сервер по API и асинхронной обработке их с использованием Celery.


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/astatr1/Django-REST-API.git
```

```
cd drfapi
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Применить миграции:
```
python manage.py migrate
```

Запустить проект:
```
python manage.py runserver
```

### Выполнение GET запроса:

Выполнить GET запрос по пути http://127.0.0.1:8000/api/files/ и получить результат:

![get](https://github.com/astatr1/Django-REST-API/assets/142535647/1fc632f0-00d9-429c-b0fd-46110a78cfdd)

### Выполнение POST запроса:

Выполнение POST запроса осуществляется для сохранения переданного файла на сервер.

Шаги выполнения POST запроса:

Запустить Redis в контейнере:
```
docker run -it --rm --name redis -p 6379:6379 redis
```

Запустить Celery :
```
celery -A drfapi worker -l info 
```

Выполнить POST запрос передав пару ключ: 'file' и значение: ссылку на локальный файл. 
![post](https://github.com/astatr1/Django-REST-API/assets/142535647/041b207c-6dba-498c-9c9c-8680741b7e54)
