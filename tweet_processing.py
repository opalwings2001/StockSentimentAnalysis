import pandas as pd
import nltk
#from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer
import tweet_main
#
# df = main.df
#df = pd.read_csv("hackhers_sample2.csv")


def dataframe_cleaner(df):
    df_eng = df.loc[df["lang"] == "en"].reset_index()
    regexp = RegexpTokenizer('\w+')
    df_eng['text_token'] = df_eng["text"].apply(regexp.tokenize)

    # list of english stop words
    stopwords = nltk.corpus.stopwords.words('english')
    my_stopwords = ["@GOOG"]
    stopwords.extend(my_stopwords)

    df_eng['text_token'] = df_eng['text_token'].apply(lambda x: [item for item in x if item not in stopwords])

    df_eng['text_string'] = df_eng['text_token'].apply(lambda x: ' '.join([item for item in x if len(item)>2]))

    print(df_eng.head(10))

    print(list(df_eng.columns.values))

    all_words = ' '.join([word for word in df_eng['text_string']])
    tokenized_words = nltk.tokenize.word_tokenize(all_words)
    #print(tokenized_words)

    fdist = FreqDist(tokenized_words)
    print(fdist)

    df_eng["text_string_fdist"] = df_eng["text_token"].apply(lambda x: ' '.join([item for item in x if fdist[item] >= 2]))
    print(df_eng[['text', 'text_token', 'text_string', 'text_string_fdist']].head())

    nltk.download('wordnet')
    nltk.download('omw-1.4')

    wordnet_lem = WordNetLemmatizer()

    df_eng["text_string_lem"] = df_eng["text_string_fdist"].apply(wordnet_lem.lemmatize)
    df_eng['is_equal']= (df_eng['text_string_fdist']==df_eng['text_string_lem'])
    print(df_eng.is_equal.value_counts())

    print(df_eng.head())

    nltk.download('vader_lexicon')
    from nltk.sentiment import SentimentIntensityAnalyzer

    analyzer = SentimentIntensityAnalyzer()

    df_eng["polarity"] = df_eng["text_string_lem"].apply(lambda x: analyzer.polarity_scores(x))
    print(df_eng.tail(10))

    print(list(df_eng.columns.values))
    df = pd.concat([df_eng.drop(["id", "polarity"], axis =1), df_eng['polarity'].apply(pd.Series)], axis=1)

    print(df[["neg", "neu", "pos", "compound"]].head())

    df["sentiment"] = df["compound"].apply(lambda x: 'positive' if x > 0 else 'neutral' if x == 0 else 'negative')

    print(df[["sentiment"]].head())

    df.to_csv("sentiment.csv")
    return df

