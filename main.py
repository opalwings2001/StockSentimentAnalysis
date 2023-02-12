import base64
import io
import os

from flask import Flask, render_template, request
import twitter_information_parsing as t
import sentiment_graphs as s
import tweet_main as tm
import tweet_processing as tp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg, FigureCanvasBase
import plotly
import json


app = Flask(__name__, template_folder='templates', static_folder="static")


@app.route('/', methods=['GET', 'POST'])
def test():
    if os.path.exists('./static/images/pieChart.png'):
        os.remove('./static/images/pieChart.png')

    if os.path.exists('./static/images/wordCloud.png'):
        os.remove('./static/images/wordCloud.png')

    if request.method == 'POST':
        symbol = request.form.get('myTicker')
        data = tm.make_query(symbol)
        cleaned = tp.dataframe_cleaner(data)
        pie_chart = s.piechart(cleaned,symbol)
        word_cloud = s.wordcloud(cleaned)

        stock_df = t.get_stock_df(symbol, "compact")

        stock_chart = t.generate_chart(symbol, stock_df)
        graphJSON = json.dumps(stock_chart, cls=plotly.utils.PlotlyJSONEncoder)

        return render_template('twitter_template.html', graphJSON=graphJSON, pieChart='./static/images/pieChart.png', wordCloud='./static/images/wordCloud.png')

    return render_template('twitter_template.html')


if __name__ == '__main__':
    app.debug=True
    app.run()
