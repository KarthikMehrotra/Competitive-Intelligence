# Visualization - Topics
# fig, ax = plt.subplots()
# ax.barh(range(num_topics), [1] * num_topics, align='center', color='lightgray', edgecolor='k')
# ax.set_yticks(range(num_topics))
# ax.set_yticklabels([f'Topic {i}' for i in range(num_topics)])
# ax.invert_yaxis()
# ax.set_xlabel('Word Importance')
# ax.set_title('Most Relevant Topics')

# for i, topic in enumerate(topics):
#     words = topic[1].split(' + ')
#     words = [w.split('*')[1][1:-1] for w in words]
#     ax.text(0.05, i, ' + '.join(words), ha='left', va='center')

# plt.tight_layout()
# plt.show()