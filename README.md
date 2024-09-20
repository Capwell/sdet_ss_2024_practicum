# sdet_ss_2024

## Установка
Клонируйте репозиторий:

```git clone ```

Перейдите в директорию проекта и установите зависимости

```poetry install```

При необходимости выбрерите локальную версию python (требуется установленный pyenv)

```pyenv local 3.10.14```

## Запуск тестов:
В директории проекта выполните команду для запуска

Все тесты

```poetry run pytest -n auto```

С подробным выводом в консоль

```poetry run pytest -n auto -vv```

С логированием в allure:

```poetry run pytest -n auto --alluredir=./allure-results```

```allure serve ./allure-results```
