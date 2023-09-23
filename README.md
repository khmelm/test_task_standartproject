# Тестовое задание на позицию Дата-Инженер в компанию СтандартПроект

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Django](https://img.shields.io/badge/Django-4.x-green) ![Pandas](https://img.shields.io/badge/Pandas-1.x-orange)

C полным текстом тестового задания можно ознакомится в файле task.txt

## I Часть

### Описание функционирования созданного сервиса

С помощью библиотеки Pandas и фрэймворка Django REST Framework реализован web-сервис, который будет встроен в работу продуктивной системы. В сторону сервиса направляется массив данных, а в ответ сервис возвращает ответ из функции pick_regno.

### Объяснение особенностей реализации

а) Сервер по адресу http://127.0.0.1:8000/api/data/ принимает на вход csv-файл, обрабатывает его во вью и вызывает вспомогательную функцию для извлечения данных 'utils.py' из директории 'services'.
б) Далее из функции utils.py вызывается скрипт от ML-разработчика, который в свою очередь вызывает модель и производит расчет значения "y".
в) Когда функция завершает свою работу, рассчитанные в модели данные возвращаются в формате Json.

### Объяснение причины реализации

a) Удобство обработки запросов: Django предоставляет инструменты для обработки HTTP-запросов, включая POST-запросы с передачей файлов.
б) Мощная система маршрутизации: Django имеет мощную систему маршрутизации URL, которая позволяет легко определить, какой обработчик должен вызываться при загрузке файла.
в) Библиотека Pandas, в свою очередь, упрощает обработку CSV-файлов в Django-приложении.

## II Часть

### Активирование и тестирование кода.

1. В рабочей области клонировать файлы из директории

```git
git clone https://github.com/khmelm/test_task_standartproject.git
```

2. Установить и активировать виртуальное окружение в рабочей области

```python
python -m venv venv
. venv/bin/activate #для linux
```

или

```python
.venv/scripts/activate #для windows
```

3. Установить зависимости из файла requirements.txt

```python
pip install -r requirements.txt
```

4. Перейти в папку 'rest_service' и применить миграции

```python
python manage.py migrate
```

5. Запустить приложение

```python
python manage.py runserver
```

6. В Postman открыть json-коллекцию из директории 'postman_collection' для отправки запроса по адресу http://127.0.0.1:8000/api/data/. В body передать ключ - 'file_path' и сам путь до csv-файла

7. Отправить запрос и получить рассчетные данные в Json-формате.
