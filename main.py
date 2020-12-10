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

# ------------------------------ Server config -----------------------------

HOST = '172.17.0.1'
PORT = 5000

server = Flask(__name__)    

@server.route('/', methods=['POST'])
def home():
    callback(request.json)
    return Response(status=200)

# ------------------------------ Dash config -------------------------------

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

# ------------------------------ Main --------------------------------------

if __name__ == '__main__':
    app.run_server(host=HOST, port=PORT)