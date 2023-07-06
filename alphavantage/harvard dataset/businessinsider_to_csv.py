import json
import csv

# Read JSON data from file
with open(r'businessinsider.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Define the desired field names for CSV
fieldnames = ['id', 'date', 'source', 'title', 'content', 'author', 'url', 'published', 'published_utc', 'collection_utc']

# Create a CSV file and write header row
with open('output.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # Write each JSON object as a CSV row
    for item in data:
        writer.writerow(item)
