import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=NASDX&outputsize=full&apikey=9GEPM841QDY4HGPG&datatype=csv'

response = requests.get(url)
data = response.content.decode('utf-8')

file_path = r'C:\Users\karth\AppData\Local\Programs\Python\Python311\Coforge\alphavantage\index data\s&p500_data.csv'

with open(file_path, 'w') as file:
    file.write(data)

print(f"Data saved to: {file_path}")
