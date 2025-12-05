# Парсинг перечня политических партий

Этот проект реализует парсинг списка политических партий с сайта [minjust.gov.ru](https://minjust.gov.ru/pages/politicheskie-partii/), извлекает ссылки на документы партий и сохраняет их в структуру данных Python (списки, словари).

## Требования

Для работы с проектом необходимы следующие зависимости:

- Python >= 3.x
- BeautifulSoup4 >= 4.12.0


---

## Установка и запуск

# 1. Клонировать репозиторий

``` bash
git clone https://github.com/Overyourhead/parsing-political-parties.git
cd parsing-political-parties
```

# 2. Создать виртуальное окружение

``` bash
python3 -m venv venv
source venv/bin/activate       # macOS / Linux
# или
venv\Scripts\activate        # Windows
```

# 3. Установить зависимости

``` bash
pip install -r requirements.txt
```

# 4. Запустить парсер

``` bash
python3 parse_parties.py
```

Результат появится в консоли и сохранится в файле JSON.

