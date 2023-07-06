import os
import pandas as pd
import numpy as np
import gensim
from gensim import corpora
from gensim.models import LdaModel
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pyLDAvis.gensim
import pickle
import webbrowser

# Step 1: Data Preprocessing
df = pd.read_csv('alphavantage/apple/apple_merged.csv')
df = df.dropna(subset=['content'])  # Data cleaning

# Remove stop words, symbols and unnecessary info from the content field
stop_words = set(stopwords.words('english'))
df['content'] = df['content'].apply(lambda x: ' '.join([word for word in word_tokenize(x) if word.lower() not in stop_words and word.isalpha()]))

documents = df['content'].tolist()

# Tokenization and create document-term matrix
texts = [[word for word in document.lower().split()] for document in documents]
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# LDA Model Training
num_topics = 10  # Set the desired number of topics
lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, passes=10)

# Print the Keyword in the 10 topics
print(lda_model.print_topics())

# Most relevant topics
topics = lda_model.print_topics(num_words=2)

# Correlation Matrix
topic_distribution = lda_model.get_document_topics(corpus)
correlation_matrix = np.zeros((num_topics, num_topics))

for doc_topics in topic_distribution:
    for topic1, weight1 in doc_topics:
        for topic2, weight2 in doc_topics:
            correlation_matrix[topic1][topic2] += weight1 * weight2

# Normalize matrix
correlation_matrix /= np.sum(correlation_matrix)

# Visualization
LDAvis_data_filepath = os.path.join('C:\\Users\\karth\\AppData\\Local\\Programs\\Python\\Python311\\Coforge\\alphavantage\\apple', 'ldavis_prepared_' + str(num_topics))

# Generate and save the LDA visualization data
LDAvis_prepared = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary)
with open(LDAvis_data_filepath, 'wb') as f:
    pickle.dump(LDAvis_prepared, f)

# Save the pyLDAvis visualization as an HTML file
pyLDAvis.save_html(LDAvis_prepared, os.path.join('C:\\Users\\karth\\AppData\\Local\\Programs\\Python\\Python311\\Coforge\\alphavantage\\apple', 'ldavis_prepared_' + str(num_topics) + '.html'))

# Open the saved HTML file in the default web browser
webbrowser.open('file://' + os.path.abspath(LDAvis_data_filepath + '.html'))
