from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin


def fix_url(url):
    if not url:
        return None
    
    url = url.strip()
    base_url = 'https://minjust.gov.ru'
    
    if url.startswith('/'):
        url = urljoin(base_url, url)
    elif not url.startswith('http'):
        url = urljoin(base_url + '/', url)
    
    if url.startswith('http://'):
        url = url.replace('http://', 'https://', 1)
    
    return url


def parse_parties(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    parties_list = soup.find('div', id='section-765')
    
    if not parties_list:
        return []
    
    items = parties_list.find_all('li')
    
    parties = []
    
    for item in items:
        link = item.find('a')
        
        if link:
            name = link.get_text(strip=True)
            
            doc_url = link.get('href', '')
            doc_url = fix_url(doc_url) if doc_url else None
            
            parties.append({
                'name': name,
                'doc_url': doc_url
            })
    
    return parties


def main():
    html_file = 'Minjust.html'
    
    parties = parse_parties(html_file)
    
    if not parties:
        print("Партии не найдены!")
        return
    
    print(f"\nНайдено партий: {len(parties)}\n")
    
    print("Результаты:")
    print("=" * 80)
    for i, party in enumerate(parties, 1):
        print(f"\n{i}. {party['name']}")
        print(f"   Документ: {party['doc_url'] or 'Не указан'}")
    
    output_file = 'parties.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(parties, f, ensure_ascii=False, indent=2)
    
    print(f"\n\nДанные сохранены в файл: {output_file}")


if __name__ == '__main__':
    main()