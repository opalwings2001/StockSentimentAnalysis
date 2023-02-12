from flask import Flask, render_template, request
import twitter_information_parsing as t
import plotly
import json


app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        symbol = request.form.get('myTicker')
        stock_df = t.get_stock_df(symbol, "compact")

        fig = t.generate_chart(symbol, stock_df)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        return render_template('twitter_template.html', graphJSON=graphJSON)
    return render_template('twitter_template.html')


if __name__ == '__main__':
    app.run()
