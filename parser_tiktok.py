import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import csv
import os

url = 'your link'  

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.37',
}

def unix_to_human(unix_time):
    try:
        dt = datetime.fromtimestamp(unix_time)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        return f"Error: {e}"

def clean_text(text):
    if text is None:
        return ""
    return text.encode('utf-8').decode('utf-8')

def extract_data(html):
    data = {
        'id_video': None,
        'duration_seconds': None,
        'text_part': None,
        'hashtags': None,
        'human_time': None,
        'author_followers': None,
        'author_likes': None,
        'id_sound': None,
        'views': None,
        'likes': None
    }
    
    try:
        match = re.search(r'"preciseDuration":\s*(\d+)', html)
        data['duration_seconds'] = int(match.group(1)) if match else None

        match = re.search(r'"desc":\s*"([^"]+)"', html)
        if match:
            desc = match.group(1)
            data['text_part'] = clean_text(re.sub(r'#\w+', '', desc).strip())
            hashtags = re.findall(r'#(\w+)', desc)
            data['hashtags'] = clean_text(', '.join(hashtags))

        match = re.search(r'"createTime":\s*(\d+)', html)
        if match:
            create_time = int(match.group(1))
            data['human_time'] = unix_to_human(create_time)

        match = re.search(r'"followerCount":\s*(\d+)', html)
        data['author_followers'] = int(match.group(1)) if match else None

        match = re.search(r'"heartCount":\s*(\d+)', html)
        data['author_likes'] = int(match.group(1)) if match else None

        match = re.search(r'"music":{"id":"\s*(\d+)', html)
        data['id_sound'] = int(match.group(1)) if match else None

        match = re.search(r'"playCount":\s*(\d+)', html)
        data['views'] = int(match.group(1)) if match else None

        match = re.search(r'"diggCount":\s*(\d+)', html)
        data['likes'] = int(match.group(1)) if match else None
        
    except Exception as e:
        print(f"Ошибка при извлечении данных: {e}")
    
    return data

def get_next_id(filename='tiktok_data.csv'):
    if not os.path.exists(filename):
        return 1
    
    with open(filename, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        if not rows:
            return 1
        last_id = int(rows[-1]['id_video'])
        return last_id + 1

def save_to_csv(data, filename='tiktok_data.csv'):
    fieldnames = [
        'id_video',
        'duration_seconds',
        'text_part',
        'hashtags',
        'human_time',
        'author_followers',
        'author_likes',
        'id_sound',
        'views',
        'likes'
    ]
    
    try:
        data['id_video'] = get_next_id(filename)
        file_exists = os.path.isfile(filename)
        
        with open(filename, 'a', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader()
            
            writer.writerow(data)
        
        print(f"Данные успешно сохранены в {filename} (ID: {data['id_video']})")
    except Exception as e:
        print(f"Ошибка при сохранении в CSV: {e}")

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    
    with open('tiktok_page.txt', 'w', encoding='utf-8') as file:
        file.write(str(soup))
    print("HTML сохранен в файл 'tiktok_page.txt'")
    
    html = str(soup)
    data = extract_data(html)
    
    for key, value in data.items():
        print(f"{key}: {value}")
    
    save_to_csv(data)

except requests.exceptions.RequestException as e:
    print(f"Ошибка при запросе: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")