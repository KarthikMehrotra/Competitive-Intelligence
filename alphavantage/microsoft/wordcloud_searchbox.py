import os
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def update_wordcloud(event=None):
    search_term = search_entry.get()

    # Filter verbs based on search term
    filtered_verbs = [verb for verb in verbs if search_term.lower() in verb.lower()]

    # Generate word cloud based on filtered verbs
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(filtered_verbs))

    # Update the word cloud image
    figure.clear()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    canvas.draw()


# Load the extracted data from JSON file
json_file_path = r'C:\Users\karth\AppData\Local\Programs\Python\Python311\Coforge\alphavantage\microsoft\extracted_data_gcp_microsoft.json'
with open(json_file_path, 'r') as file:
    extracted_data = json.load(file)

# Extract verbs from the data
verbs = []
for item in extracted_data:
    verbs.extend(item['verbs'])

# Create a window
window = tk.Tk()
window.title('Word Cloud')

# Create a search box
search_entry = tk.Entry(window)
search_entry.pack(side='top', padx=10, pady=10)

# Create a filter button
filter_button = tk.Button(window, text='Filter', command=update_wordcloud)
filter_button.pack(side='top', padx=10, pady=5)

# Create the initial word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(verbs))

# Create a canvas to display the word cloud image
figure = plt.figure(figsize=(8, 4))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
canvas = FigureCanvasTkAgg(figure, master=window)
canvas.get_tk_widget().pack(side='top', padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()
