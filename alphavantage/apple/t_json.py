import json
import requests
from bs4 import BeautifulSoup

api_key = '9GEPM841QDY4HGPG'
folder_path = r'C:\Users\karth\AppData\Local\Programs\Python\Python311\Coforge\alphavantage\apple'

url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&topics=earnings,merger&acquistions,economy_macro,financial_markets&time_from=20230508T0130&time_to=20230608T0130&apikey=9GEPM841QDY4HGPG'
response = requests.get(url)
data = response.json()

# Specify the path for the JSON file
json_file_path = folder_path + '\\t.json'

extracted_data = []

for item in data['feed']:
    title = item['title']
    url = item['url']
    time_published = item.get('publishedDate', '')
    content = ""

    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        lines = soup.get_text().splitlines()
        content = ' '.join(line.strip() for line in lines if line.strip())
    except Exception as e:
        print(f"Error occurred while scraping {url}: {str(e)}")

    # Add the URL as the second column
    item['url'] = url
    item['content'] = content

    # Add the modified item to the extracted data
    extracted_data.append(item)

# Save the data to the JSON file
with open(json_file_path, 'w') as file:
    json.dump(extracted_data, file, indent=2)

print('Data saved to JSON file:', json_file_path)
