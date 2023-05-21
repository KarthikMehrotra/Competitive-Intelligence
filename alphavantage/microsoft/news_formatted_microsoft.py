import os
import configparser
import requests
from bs4 import BeautifulSoup
import json

api_key = '9GEPM841QDY4HGPG'
folder_path = r'C:\Users\karth\AppData\Local\Programs\Python\Python311\Coforge\alphavantage\microsoft'


url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=MSFT&apikey=9GEPM841QDY4HGPG'
r = requests.get(url)
data = r.json()

items = data['feed']

extracted_data = []

for item in items:
    url = item['url']
    content = ""

    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        lines = soup.get_text().splitlines()
        content = ' '.join(line.strip() for line in lines if line.strip())
    except Exception as e:
        print(f"Error occurred while scraping {url}: {str(e)}")

    extracted_item = {
        'url': url,
        'content': content
    }
    extracted_data.append(extracted_item)

json_file_path = os.path.join(folder_path, 'extracted_data_microsoft.json')

with open(json_file_path, 'w') as file:
    json.dump(extracted_data, file)

print('Data extracted')
