import os.path

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import wordcloud
from wordcloud import WordCloud
from datetime import date
import tweet_processing

#df = pd.read_csv("sentiment.csv")

matplotlib.use('agg')
def piechart(df,symbol):
    # print(df.head(10))

    today = date.today()
    chart_title = f"{symbol.upper()} Tweets Sentiment Distribution on {today}"

    count_neg = df.groupby("sentiment").size()[0]
    count_neutral = df.groupby("sentiment").size()[1]
    count_positive = df.groupby("sentiment").size()[2]

    sentiment_counts = np.array([count_neg, count_neutral, count_positive])

    plt.clf()

    pieC = plt.figure
    labels = ["Negative", "Neutral", "Positive"]
    colors = ["#f86479", "#f7f77b", "#62e1ac" ]
    plt.pie(sentiment_counts, labels = labels, colors = colors)
    plt.legend(title = "Sentiments", loc = "upper left")
    plt.title(chart_title)

    # if os.path.exists('./static/images/pieChart.png'):
    #     os.remove('./static/images/pieChart.png')
    #     plt.savefig('./static/images/pieChart.png')
    # else:
    plt.savefig('./static/images/pieChart.png')

    return pieC


def wordcloud(df):
    word_string = ""
    for tweet in df["text_string_lem"]:
        word_string += tweet

    plt.clf()

    word = plt.figure
    wordCloud = WordCloud(min_word_length=3, height=1000, width=1500, background_color="white").generate(word_string)
    plt.axis("off")


    plt.imshow(wordCloud, interpolation="bilinear")

    # if os.path.exists('./static/images/wordCloud.png'):
    #     os.remove('./static/images/wordCloud.png')
    #     plt.savefig('./static/images/wordCloud.png')
    # else:
    plt.savefig('./static/images/wordCloud.png')

    return word



