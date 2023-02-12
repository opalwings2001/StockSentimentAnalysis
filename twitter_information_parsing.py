import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import plotly
import requests


def get_stock_df(symbol, output_size):
    symbol = symbol.upper()
    output_size = output_size.lower()

    api_key = 'AHOJ4KYYY0BNKZU1'
    base_url = 'https://www.alphavantage.co/query?'
    function = 'TIME_SERIES_DAILY_ADJUSTED'

    params = {'function': function,
              'symbol': symbol,
              'datatype': 'csv',
              'apikey': api_key,
              'outputsize': output_size}

    response = requests.get(base_url, params)

    # save csv to file
    with open('stock_data.csv', 'wb') as file:
        file.write(response.content)

    stock_df = pd.read_csv('stock_data.csv')  # create pandas df

    return stock_df


ibm_pd = get_stock_df("ibm", "Compact")


def generate_chart(symbol, df_stocks):

    fig_title = f'{symbol.upper()} Time Series Chart'
    layout_fig = go.Layout(xaxis=dict(title='Data') , title=fig_title)

    fig_data = go.Scatter(x=df_stocks['timestamp'], y=df_stocks['close'])
    fig = go.Figure(data=fig_data, layout=layout_fig)

    return fig


def get_tweets(stock_df):

    today_stock_data = stock_df.head(1)

    return today_stock_data





