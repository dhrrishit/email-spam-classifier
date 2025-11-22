import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

def get_data_distribution(df):
    return df['target'].value_counts()

def get_most_common_words(df, target):
    words = []
    for msg in df[df['target'] == target]['transformed_text'].tolist():
        for word in msg.split():
            words.append(word)
    
    return pd.DataFrame(Counter(words).most_common(30))

def plot_pie_chart(counts):
    fig, ax = plt.subplots()
    ax.pie(counts, labels=['Ham', 'Spam'], autopct='%0.2f', colors=['#22c55e', '#ef4444'])
    return fig

def plot_wordcloud(df, target):
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    spam_wc = wc.generate(df[df['target'] == target]['transformed_text'].str.cat(sep=" "))
    fig, ax = plt.subplots()
    ax.imshow(spam_wc)
    ax.axis('off')
    return fig
