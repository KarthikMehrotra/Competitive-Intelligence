import os
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Path to the JSON file
json_file_path = r'C:\Users\karth\AppData\Local\Programs\Python\Python311\Coforge\alphavantage\microsoft\extracted_data_gcp_microsoft.json'

# Load the JSON data
with open(json_file_path, 'r') as file:
    extracted_data = json.load(file)

# Extract verbs from the data
verbs = []
for item in extracted_data:
    verbs.extend(item['verbs'])

# Create a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(verbs))

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
