import csv
import json

json_file_path = r'C:\Users\karth\AppData\Local\Programs\Python\Python311\Coforge\alphavantage\apple\apple_may.json'
csv_file_path = r'C:\Users\karth\AppData\Local\Programs\Python\Python311\Coforge\alphavantage\apple\apple_may.csv'

# Open the JSON file and load the data
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Open the CSV file in write mode
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the column headers to the CSV file
    writer.writerow(['company_name', 'url', 'time_published', 'topic', 'relevance_score',
                     'ticker', 'ticker_relevance_score', 'ticker_sentiment_score', 'ticker_sentiment_label'])

    # Write each news item as a row in the CSV file
    for item in data:
        title = item.get('title', '')
        time_published = item.get('time_published', '')
        url = item.get('url', '')
        topic = ''
        relevance_score = ''
        ticker = ''
        ticker_relevance_score = ''
        ticker_sentiment_score = ''
        ticker_sentiment_label = ''

        topics = item.get('topics', [])
        if topics:
            topic = topics[0].get('topic', '')
            relevance_score = topics[0].get('relevance_score', '')

        ticker_sentiment = item.get('ticker_sentiment', [])
        if ticker_sentiment:
            ticker = ticker_sentiment[0].get('ticker', '')
            ticker_relevance_score = ticker_sentiment[0].get('relevance_score', '')
            ticker_sentiment_score = ticker_sentiment[0].get('ticker_sentiment_score', '')
            ticker_sentiment_label = ticker_sentiment[0].get('ticker_sentiment_label', '')

        # Write the row to the CSV file
        writer.writerow(['Apple', url, time_published, topic, relevance_score,
                         ticker, ticker_relevance_score, ticker_sentiment_score, ticker_sentiment_label])
