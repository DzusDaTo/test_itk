# Django REST API - ITK проект

Это Django проект, реализующий API для загрузки и управления данными базовых станций с использованием Django REST Framework. Также в проекте есть интерфейс Swagger для удобной работы с документацией API.

## Функции

1. **POST запрос**: Загружает Excel файл (`example.xlsx`) и сохраняет данные в базу данных PostgreSQL.
2. **GET запрос (JSON)**: Возвращает данные базовых станций в формате JSON.
3. **GET запрос (HTML)**: Отображает данные базовых станций в виде HTML таблицы.

## Технологии

- Django 5.1.3
- Django REST Framework
- PostgreSQL
- drf-yasg (Swagger UI)
- Pandas (для чтения и обработки Excel файлов)
- Python 3.11

## Установка

### 1. Клонировать репозиторий

```
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
```
### 2. Установить зависимости
```
pip install -r requirements.txt
```

### 3. Создайтке и примените миграции
```
python manage.py makemigrations
python manage.py migrate
```

### 4. Запустите сервер 
```
python manage.py runserver
```

## API эндпоинты

- **POST `/api/upload/`**: Загружает Excel файл и сохраняет данные в базе данных.
- **GET `api/data/json/`**: Возвращает данные базовых станций в формате JSON.
- **GET `api/data/html/`**: Возвращает данные базовых станций в виде HTML таблицы.
- **GET `/swagger/`**: Доступ к Swagger UI для документации API.

## Пример файла (example.xlsx)

| ne    | address                    | coordinates   | technology          | status |
|-------|----------------------------|---------------|---------------------|--------|
| BS_001| г. Новосибирск, ул. X, д. 1 | 43.5, 53.5    | lte, gsm            | 0      |
| BS_002| г. Новосибирск, ул. X, д. 2 | 43.5, 53.6    | umts                | 0      |
| BS_003| г. Новосибирск, ул. X, д. 3 | 43.5, 53.7    | gsm, umts           | 1      |


