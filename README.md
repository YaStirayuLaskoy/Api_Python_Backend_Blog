# Api_Final_YaTube

# Описание
Апи для YaTube

# Технологии
Самые последние, внеземные, засекреченные, поддерживаемые искусственным интеллектом и курированные Илоном Маском!

### Авторы
Йа и мой Ревьюер Денис Волох.

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram2plus.git
```

```
cd kittygram2plus
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Пример запросов к API:

Получить список всех постов (GET):

```
http://127.0.0.1:8000/api/v1/posts/
```

Получить один пост (GET):

```
http://127.0.0.1:8000/api/v1/posts/1/
```

Получить список групп (GET):

```
http://127.0.0.1:8000/api/v1/groups/
```

Зарегистрироваться (POST):

```
http://127.0.0.1:8000/auth/users/
```

Документация (GET):

```
http://127.0.0.1:8000/redoc/
```
