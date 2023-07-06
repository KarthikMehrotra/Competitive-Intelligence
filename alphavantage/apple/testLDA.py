import nltk
nltk.download('stopwords')
nltk.download('punkt')
import pandas as pd
import numpy as np
import gensim
from gensim import corpora
from gensim.models import LdaModel
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

# Step 1: Data Preprocessing
df = pd.read_csv(r'alphavantage\apple\apple_merged.csv')
df = df.dropna(subset=['content'])  # Data cleaning

# Remove stop words, symbols and uncessary info from the content field
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

# Most relevant topics
topics = lda_model.print_topics(num_words=2)  # Set the number of words per topic

# Correlation Matrix
topic_distribution = lda_model.get_document_topics(corpus)
correlation_matrix = np.zeros((num_topics, num_topics))

for doc_topics in topic_distribution:
    for i, (topic1, weight1) in enumerate(doc_topics):
        for j, (topic2, weight2) in enumerate(doc_topics):
            correlation_matrix[topic1][topic2] += weight1 * weight2

# Normalize matrix
correlation_matrix /= np.sum(correlation_matrix)

# Visualization - Topics
fig, ax = plt.subplots()
ax.barh(range(num_topics), [1] * num_topics, align='center', color='lightgray', edgecolor='k')
ax.set_yticks(range(num_topics))
ax.set_yticklabels([f'Topic {i}' for i in range(num_topics)])
ax.invert_yaxis()
ax.set_xlabel('Word Importance')
ax.set_title('Most Relevant Topics')

for i, topic in enumerate(topics):
    words = topic[1].split(' + ')
    words = [w.split('*')[1][1:-1] for w in words]
    ax.text(0.05, i, ' + '.join(words), ha='left', va='center')

plt.tight_layout()
plt.show()

# Visualization - Correlation Matrix
fig, ax = plt.subplots()
im = ax.imshow(correlation_matrix, cmap='coolwarm')
ax.set_xticks(range(num_topics))
ax.set_yticks(range(num_topics))
ax.set_xticklabels([f'Topic {i}' for i in range(num_topics)], rotation=45, ha='right')
ax.set_yticklabels([f'Topic {i}' for i in range(num_topics)])
ax.set_xlabel('Topic')
ax.set_ylabel('Topic')
ax.set_title('Correlation Matrix')

for i in range(num_topics):
    for j in range(num_topics):
        text = ax.text(j, i, f'{correlation_matrix[i, j]:.2f}', ha='center', va='center', color='black')

plt.colorbar(im, ax=ax)
plt.tight_layout()
plt.show()
