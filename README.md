# Инструкция по запуску проекта

## Основные настройки проекта

### Склонируйте репозиторий с помощью git команды:

```
git clone https://github.com/neeearina/jobik_api.git
```

### Создайте виртуальное окружение и активируйте его:

```
python3 -m venv venv 
```

```
source venv/bin/activate 
```

### Зависимости проекта

Установить зависимости для прод режима:

```
pip install -r requirements/prod.txt
```

для дев режима (включает в себя установку продовых зависимостей):

```
pip install -r requirements/dev.txt
```

для тестов:

```
pip install -r requirements/test.txt
```

### Переменные виртуального окружения

Создайте в корнейвой директории проекта файл .env. Заполните файл переменными
окружения по примеру файла example_env, расположенный также в корневой
директории проекта.

### Секретный ключ

Получить данные секретного ключа для проекта можно с помощью таких команд:

```
from django.core.management.utils import get_random_secret_key
```

```
get_random_secret_key()
```

## Последующие команды выполняются из директории проекта jobik_api

### Выполните миграции для создания таблиц в БД:

```
python manage.py migrate
```

### Актуальная ER диаграмма со структурой БД по ссылке

[ERD](https://dbdiagram.io/d/656488923be1495787ceca36)

### Загрузите фикстуры в БД:

```
python manage.py loaddata fixtures/categories.json
```

```
python manage.py loaddata fixtures/professions.json
```

### Создайте пользователя для входа в admin-панель:

После выполнения команды заполните все нужные поля в консоли (юзернейм, почта,
пароль и т.д.)

```
python manage.py createsuperuser
```

### Запустите проект с помощью следующей команды и перейдите по ссылке в терминале:

```
python manage.py runserver
```





