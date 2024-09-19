# FastAPI Llama Project

## Описание

Это FastAPI приложение, использующее модель LLama для генерации текстовых ответов. Приложение имеет один POST эндпоинт `/generate/`, который принимает сообщение и возвращает сгенерированный ответ.


## Установка и запуск

Клонируйте репозиторий:
```sh
   git clone https://github.com/nellialeksanian/llama-fastapi.git
   cd llama-fastapi
```

Установите зависимости:
```sh
pip install -r requirements.txt
```
Запустите сервер:
```sh
uvicorn app.main:app
```
### Запуск с Docker

Соберите Docker образ:
```sh
docker build --tag "llama-fast-api" .
```
Запустите контейнер:
```sh
docker run -it -p 8000:8000/tcp llama-fast-api 
```


