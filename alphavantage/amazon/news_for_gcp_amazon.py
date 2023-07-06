import os
import requests
from bs4 import BeautifulSoup
import csv
import spacy
from google.cloud import language_v1
from google.oauth2.service_account import Credentials

api_key = '9GEPM841QDY4HGPG'
folder_path = r'C:\Users\karth\AppData\Local\Programs\Python\Python311\Coforge\alphavantage\amazon'

# Set the path to your service account key file
keyfile_path = r'C:\Users\karth\AppData\Local\Programs\Python\Python311\Coforge\gcp\flawless-augury-387108-9fce49a6b23c.json'

# Define the scopes for authentication
SCOPES = ['https://www.googleapis.com/auth/cloud-platform']

# Create the credentials object
credentials = Credentials.from_service_account_file(keyfile_path, scopes=SCOPES)

# Create a client for the Cloud Natural Language API
client = language_v1.LanguageServiceClient(credentials=credentials)

nlp = spacy.load("en_core_web_sm")

url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=SIVBQ&topics=earnings,merger&acquistions,economy_macro,financial_markets&time_from=20230508T0130&time_to=20230608T0130&apikey=9GEPM841QDY4HGPG'
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

    # Extract verbs
    doc = nlp(content)
    verbs = [
        token.lemma_
        for token in doc
        if token.pos_ == 'VERB'
    ]

    extracted_item = {
        'url': url,
        'entities': entities,
        'verbs': verbs,
    }
    extracted_data.append(extracted_item)

# Define the output file name
csv_file_name = 'extracted_data_entity_verbs_may_sivbq_.csv'

csv_file_path = os.path.join(folder_path, csv_file_name)

with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['url', 'entity', 'salience', 'verb', 'company_name'])

    for item in extracted_data:
        url = item['url']

        entities = item['entities']
        for entity in entities:
            name = entity['name']
            entity_type = entity['type']
            salience = entity['salience']
            writer.writerow([url, name, salience, '', 'SVB'])

        verbs = item['verbs']
        for verb in verbs:
            writer.writerow([url, '', '', verb, 'SVB'])

print('CSV file created')
