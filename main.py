from flask import Flask, render_template, request
import twitter_information_parsing as t
import sentiment_graphs as s
import tweet_main as tm
import tweet_processing as tp
import plotly
import json


app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        symbol = request.form.get('myTicker')
        data = tm.make_query(symbol)
        cleaned = tp.dataframe_cleaner(data)
        pie_chart = s.piechart(cleaned)
        # df = tm.make_query(symbol)
        # print(df)

        # stock_df = t.get_stock_df(symbol, "compact")

        # fig = t.generate_chart(symbol, stock_df)
        graph1JSON = json.dumps(pie_chart, cls=plotly.utils.PlotlyJSONEncoder)

        return render_template('twitter_template.html', graph1JSON=graph1JSON)
    return render_template('twitter_template.html')


if __name__ == '__main__':
    app.run()
