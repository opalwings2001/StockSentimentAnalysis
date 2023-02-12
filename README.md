# StockSentimentAnalysis

# **Twitter Stock Sentiment Analysis Dashboard**

## Inspiration
Our team aimed to tackle the challenge of the constantly changing stock market by developing a tool that provides quick and simple access to public sentiment towards a specific stock on social media, specifically Twitter. The tool provides real-time sentiment analysis in a user-friendly dashboard, utilizing data visualization tools and sentiment analysis algorithms. With the belief that social media sentiment can be a valuable indicator of market sentiment, we hope to empower investors with the ability to make informed decisions.

## What it does
The Twitter Stock Sentiment Analysis Dashboard allows users to input a stock ticker and receive an in-depth analysis of public sentiment towards the stock on Twitter. The dashboard generates a chart that displays the sentiment towards the stock for that exact day, which is categorized as positive, neutral, or negative. Additionally, the dashboard displays a word cloud of tweets related to the stock, emphasizing the frequently used words in the tweets. The dashboard also includes a chart that visually represents the public's perception of the stock through the analysis of the sentiment of tweets for the past couple of weeks. With this tool, users can quickly and easily access important information about the public's sentiment towards a specific stock, providing valuable insights for informed decision-making.
  

## How we built it
The development of our Twitter Stock Sentiment Analysis Dashboard involved the use of various technologies and frameworks, including Python, HTML/CSS, JavaScript, and JSON. To build the backend of the application, we utilized the Flask framework and several data processing libraries, such as Pandas, Numpy, and NLTK. To access and process Twitter data, we utilized the Tweepy library and a custom-built tweet processing module.

In order to perform sentiment analysis and generate word clouds, we used the Matplotlib and Wordcloud libraries, respectively. The visualization of the sentiment analysis results was made possible through the use of Plotly and the creation of custom sentiment graphs. Finally, we utilized the AlphaVantage API to gather stock data for our analysis.

By combining these technologies and libraries, we were able to create a seamless and functional product that provides real-time sentiment analysis in a user-friendly dashboard.

## Challenges we ran into
One of the main challenges was pulling large amounts of data from the Twitter API. We were initially using the wrong endpoints that were reserved only for elevated access users, while we only had the essential access to the Twitter API. Integrating multiple APIs (both Twitter and Alpha Vantage) and multiple libraries to perform the analysis was challenging and took us a while just to be able to seamlessly pull data. .
  

## Accomplishments that we're proud of
We developed a user-friendly dashboard that offers real-time sentiment analysis of a stock, made easy for anyone to understand through the combination of data visualization tools and sentiment analysis algorithms. The dashboard showcases a sentiment chart, a word cloud that emphasizes the frequently used words in tweets, and a sentiment chart that highlights the public's perception towards the stock.


## What we learned
In this project, we acquired knowledge about the crucial role of data pre-processing in sentiment analysis and its impact on accuracy. Additionally, we honed our skills in integrating multiple libraries and APIs to create a cohesive and functional product. It was our first time using the twitter API, which was very challenging to learn. Our work with sentiment analysis in the financial industry and its correlation with social media sentiment was very interesting, and we gained practical experience in working with large datasets, APIs and developing web applications.

## What's next for **Twitter Stock Sentiment Analysis Dashboard**

We plan on expanding our dashboard to provide more detailed analysis, and also integrating other social media platforms to provide a more comprehensive view of public sentiment. We believe that our Twitter Stock Sentiment Analysis Dashboard has the potential to help the way investors make informed decisions. We want to add more graphs and statistics on how trending the stock is and the volume of tweets pertaining to that stock. 



