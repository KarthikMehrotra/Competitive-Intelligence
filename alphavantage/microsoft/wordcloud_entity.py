import os
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Path to the JSON file
json_file_path = r'C:\Users\karth\AppData\Local\Programs\Python\Python311\Coforge\alphavantage\microsoft\extracted_data_gcp_microsoft.json'

# Load the JSON data
with open(json_file_path, 'r') as file:
    extracted_data = json.load(file)

# Extract entities and their salience scores
entity_salience = {}
for item in extracted_data:
    entities = item['entities']
    for entity in entities:
        name = entity['name']
        salience = entity['salience']
        if name not in entity_salience:
            entity_salience[name] = salience
        else:
            entity_salience[name] += salience

# Create a word cloud based on salience scores
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(entity_salience)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
