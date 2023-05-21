import os
import requests
from bs4 import BeautifulSoup
import json
from google.cloud import language_v1
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

api_key = '9GEPM841QDY4HGPG'
folder_path = r'C:\Users\karth\AppData\Local\Programs\Python\Python311\Coforge\alphavantage\microsoft'

#  the path
keyfile_path = r'C:\Users\karth\AppData\Local\Programs\Python\Python311\Coforge\gcp\flawless-augury-387108-9fce49a6b23c.json'

# Define the scopes for authentication
SCOPES = ['https://www.googleapis.com/auth/cloud-platform']

# credentials object
credentials = Credentials.from_service_account_file(keyfile_path, scopes=SCOPES)

#  client for the Cloud Natural Language API
client = language_v1.LanguageServiceClient(credentials=credentials)

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

    # Perform entity analysis
    document = {"content": content, "type_": language_v1.Document.Type.PLAIN_TEXT}
    response = client.analyze_entities(request={'document': document})
    entities = [
        {
            'name': entity.name,
            'type': language_v1.Entity.Type(entity.type_).name,
            'salience': entity.salience,
        }
        for entity in response.entities
    ]

    # Perform key phrase extraction
    response = client.analyze_entities(request={'document': document})
    key_phrases = [
        {
            'phrase': phrase.name,
            'salience': phrase.salience,
        }
        for phrase in response.entities
    ]

    extracted_item = {
        'url': url,
        'content': content,
        'entities': entities,
        'key_phrases': key_phrases
    }
    extracted_data.append(extracted_item)

json_file_path = os.path.join(folder_path, 'extracted_data_gcp_microsoft.json')

with open(json_file_path, 'w') as file:
    json.dump(extracted_data, file, indent=2)

print('Data extracted')

