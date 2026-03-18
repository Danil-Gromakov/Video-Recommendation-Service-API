# Video Recommendation Service API

Микро-сервис для персонализированных рекомендаций коротких видео на основе ML-алгоритма.

## Инструкция по сборке Docker образа

- ./Dockerfile - собирает образ, детали реализации см. файл
- ./docker-compose.yml - запускает сервис

```bash
# Перед запуском, убедитесь, что установлен docker, docker compose, git 
# sudo комада суперпользователя

# Скачать репозиторий
git clone <repository-url>

# шаг 2
sudo docker compose build

# шаг 3
sudo docker compose up -d
```

## Команды для запуска контейнера

```bash 
# Перед запуском контейнера, убедитесь, что образ собран командой build


# Запуск контейнера в режиме терминал 
sudo docker compose up

# Запуск контейнера в режиме постоянном 
sudo docker compose up -d

# Выключить контейнер 
sudo docker compose down

# При необходимости внести новые изменения в контейнер
# Такая последовательность команд пересобирает контейнер с новым кодом и запускает контейнер
sudo docker compose build 
sudo docker compose down
sudo docker compose up -d
```

## Примеры curl-запросов для проверки работы


```bash
# Проверка health-check
curl http://localhost:8000/health

# Ответ
{"status":"ok"}
```

```bash 
# Получение рекомендаций с другими данными
curl -X POST "http://localhost:8000/recommend" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 123,
    "watched_videos": ["v1", "v2"],
    "liked_categories": ["adventure",
                         "education"]
  }'

# Ответ
{"user_id":123,"recommendations":["v5","v3","v6"],"algorithm_version":"1.0"}
```


## Swagger API docs

```bash 
# Документация API

curl http://localhost:8000/docs
```

## Краткое описание ML-алгоритма

Алгоритм формирует рекомендации, комбинируя векторные представления просмотренных пользователем видео и его любимых категорий в единый вектор предпочтений. 

Затем вычисляется косинусное сходство между этим вектором и векторными представлениями непросмотренных видео для оценки их релевантности. 

В результате возвращаются идентификаторы top-N видео с наибольшим сходством.

## ML лаборатория 
./ml_algo.ipynb - Разработка алгоритма и тестирование алгоритма


## Комментарий 
Для демонстрации использоввался файл CSV ``videos_data.csv`` как псевдо БД для сервиса, в продуктовой разработке будет использована векторная БД или БД селективная для работы с векторами. 

## Команды локалной разработки 

```bash 
export DEV=1
cd app
fastapi dev main.py

```

```bash 
sudo docker compose build
sudo docker compose up

```
