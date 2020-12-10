#!/usr/bin/python3
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_leaflet as dl
import dash_table
from random import uniform as rand
from dash.dependencies import Input, Output, State
import pandas as pd
from flask import Flask, request, Response

# Local imports
import dropdown
import map

df = pd.DataFrame(
[
    ["State", "Number of Solar Plants", "Installed Capacity (MW)", "Average MW Per Plant", "Generation (GWh)"],
    ["California",289,4395,15.3,10826],
    ["Arizona",48,1078,22.5,2550],
    ["Nevada",11,238,21.6,557],
    ["New Mexico",33,261,7.9,590],
    ["Colorado",20,118,5.9,235],
    ["Texas",12,187,15.6,354],
    ["North Carolina",148,669,4.5,1162],
    ["New York",13,53,4.1,84]
]
)

server = Flask(__name__)    

@server.route('/', methods=['POST'])
def home():
    callback(request.json)
    return Response(status=200)

app = dash.Dash(__name__, server=server, prevent_initial_callbacks=True)
app.layout = html.Div([
    dl.Map(
        center=(-5.811967825768887, -34.20487439621176), 
        zoom=7, 
        children=[dl.TileLayer(), dl.LayerGroup(children=[],id="layer")],
        id="map", 
        style={
            'width': '50%', 
            'height': '100%', 
            'margin': "0", 
            "display": "block"
        }
    ),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_table={
            'max-width':'50%',
            'max-height': '100%',
            'margin': "0", 
            "display": "block"
        }
    ),
    # Increment in time
    dcc.Interval(
        id='interval-component',
        interval=1*1000, # in milliseconds
        n_intervals=0
    )
], 
style={
    'width': '100vw', 
    'height': '100vh',
    'display': 'flex-container',
    'justify-content': 'space-between',
    'align-items': 'flex-start',
})

@app.callback(
    Output("layer", "children"),
    Input("interval-component", "n_intervals"),
    State("layer", "children")
    )
def map_click(n_intervals, marks):
# def map_click(click_lat_lng):
    print(type(marks))
    if marks == None:
        marks = []
    marks.append(getMarker())

    return marks

if __name__ == '__main__':
    app.run_server()