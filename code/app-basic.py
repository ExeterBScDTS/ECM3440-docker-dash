# Run this app with `python app.py` and
# visit http://localhost:8080/ in your web browser.

# This example does not fetch data from the IoT hub, it's just a
# simple dash application to check that the Python environment is good.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

def prepare_app():
    app = Dash(__name__)

    df = pd.DataFrame({'soil_moisture':[12.0,14.6,13.2,14.4],'time':[0,1,2,3]})

    fig = px.bar(df, x='time', y='soil_moisture')

    app.layout = html.Div(children=[
        html.H1(children='A simple chart'),
        dcc.Graph(id='soil-moisture-graph',figure=fig)
    ])
    return app

if __name__ == '__main__':
    app = prepare_app()

    app.run_server(debug=False,host='0.0.0.0',port=8080)