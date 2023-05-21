import os
import configparser
import requests
from bs4 import BeautifulSoup
import json
import time

api_key = '9GEPM841QDY4HGPG'
folder_path = r'C:\Users\karth\AppData\Local\Programs\Python\Python311\Coforge\alphavantage\amazon'


run_count = 0
while run_count < 2:
    url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey=9GEPM841QDY4HGPG'
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

    json_file_path = os.path.join(folder_path, f'extracted_data_amazon_{run_count}.json')

    with open(json_file_path, 'w') as file:
        json.dump(extracted_data, file)

    print(f'Data extracted. Run count: {run_count + 1}')
    print(f'Number of extracted items: {len(extracted_data)}')

    # one hour
    time.sleep(3600)  

    run_count += 1

print('Completed.')

