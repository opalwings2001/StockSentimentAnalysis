import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import wordcloud
from wordcloud import WordCloud
import tweet_processing

#df = pd.read_csv("sentiment.csv")

def piechart(df):
    print(df.head(10))
    count_neg = df.groupby("sentiment").size()[0]
    count_neutral = df.groupby("sentiment").size()[1]
    count_positive = df.groupby("sentiment").size()[2]

    sentiment_counts = np.array([count_neg, count_neutral, count_positive])

    fig = plt.figure
    labels = ["Negative", "Neutral", "Positive"]
    colors = ["#f86479", "#f7f77b", "#62e1ac" ]
    plt.pie(sentiment_counts, labels = labels, colors = colors)
    plt.legend(title = "Sentiments", loc = "upper left")
    plt.show()
    return fig


def wordcloud(df):
    word_string = ""
    for tweet in df["text_string_lem"]:
        word_string += tweet

    fig = plt.figure
    wordCloud = WordCloud(min_word_length=3, height=1000, width=1500, background_color="white").generate(word_string)
    plt.axis("off")
    plt.imshow(wordCloud, interpolation="bilinear")
    plt.show()
    return fig



