# FastAPI Llama Project

## Описание

Это FastAPI приложение, использующее модель LLama для генерации текстовых ответов. Приложение имеет один POST эндпоинт `/generate/`, который принимает сообщение и возвращает сгенерированный ответ.


## Установка и запуск

Клонируйте репозиторий:
```sh
   git clone https://github.com/nellialeksanian/llama-fastapi.git
   cd llama-fastapi
```

Установка зависимостей:
```sh
pip install -r requirements.txt
```
Запуск сервера:
```sh
uvicorn app.main:app
```
### Запуск с Docker

Сбор Docker образа:
```sh
docker build --tag "llama-fast-api" .
```
Запуск контейнера:
```sh
docker run -it -p 8000:8000 llama-fast-api 
```


