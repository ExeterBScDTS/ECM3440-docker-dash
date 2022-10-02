# Run this app with `python app.py` and
# visit http://localhost:8080/ in your web browser.

from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import os
import subscriber

def prepare_app():
    app = Dash(__name__)

    df = pd.DataFrame({'soil_moisture':[],'time':[]})

    fig = px.bar(df, y='soil_moisture')

    app.layout = html.Div(children=[
        html.H1(children='Soil moisture chart'),
        dcc.Graph(id='soil-moisture-graph',figure=fig),
        dcc.Interval(
            id='interval-component',
            interval=2*1000, # in milliseconds
            n_intervals=0
        )
    ])
    return app


if __name__ == '__main__':

    topic = os.getenv('SERVICE_BUS_TOPIC')
    sub = os.getenv('SERVICE_BUS_SUBSCRIPTION')
    connection = os.getenv('SERVICE_BUS_CONNECTION')

    app = prepare_app()

    df = pd.DataFrame({'soil_moisture':[],'time':[]})

    receiver = subscriber.sb_connect(connection, topic, sub)

    @app.callback(Output('soil-moisture-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
    def update_graph_live(n):
        global df, receiver
     
        msgs = subscriber.sb_messages(receiver)
        for m in msgs:
            new_row = pd.Series(m)
            df = pd.concat([df, new_row.to_frame().T])
        fig = px.bar(df,  y='soil_moisture',  x='time', color="device_id", barmode="group")
        return fig

    app.run_server(debug=False,host='0.0.0.0',port=8080)