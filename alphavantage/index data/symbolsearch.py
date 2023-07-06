import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=NASDAQ&apikey=9GEPM841QDY4HGPG'
r = requests.get(url)
data = r.json()

print(data)