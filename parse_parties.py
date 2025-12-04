import requests
from bs4 import BeautifulSoup
import json

# URL страницы
url = 'https://minjust.gov.ru/pages/politicheskie-partii/'

# Заголовки, чтобы имитировать браузер
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Загружаем страницу с заголовками
response = requests.get(url, headers=headers)
response.raise_for_status()  # Проверяем, что запрос прошел успешно

# Парсим HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Найдем все ссылки на страницы партий
party_links = soup.find_all('a', href=True)

# Фильтруем нужные ссылки, выбираем только те, которые ведут на страницы партий
parties = []
for link in party_links:
    party_name = link.get_text(strip=True)  # Извлекаем название партии
    party_url = link['href']  # Извлекаем URL

    # Проверяем, чтобы ссылка была полной, если нет — добавляем базовый домен
    if not party_url.startswith('http'):
        party_url = f'https://minjust.gov.ru{party_url}'

    # Ищем ссылку на документ (например, устав)
    doc_url = None
    if 'dokumenti' in party_url:  # Примерная логика: ищем ссылки с 'dokumenti'
        doc_url = party_url

    # Сохраняем результаты
    parties.append({
        'name': party_name,
        'doc_url': doc_url or None  # Если документа нет, ставим None
    })

# Выводим результаты
print(json.dumps(parties, ensure_ascii=False, indent=4))

# Сохраняем результат в файл
with open('parties.json', 'w', encoding='utf-8') as f:
    json.dump(parties, f, ensure_ascii=False, indent=4)