#!/usr/bin/python3
import dash
from dash.dependencies import Input, Output, State
from flask import Flask, request, Response
from map import getMarker
from panels import createMainPanel

server = Flask(__name__)

@server.route('/', methods=['POST'])
def home():
    callback(request.json)
    return Response(status=200)

app = dash.Dash(
    __name__, 
    server=server, 
    prevent_initial_callbacks=True,
    meta_tags=[
        {'charset': 'utf-8'},
        {
          'name': 'viewport',
          'content': 'width=device-width, initial-scale=1.0'
        }
    ],
    title='Ofertados',
    update_title=None
)
app.layout = createMainPanel()

@app.callback(
    Output("layer", "children"),
    Input("interval-component", "n_intervals"),
    State("layer", "children"))
def map_update(n_intervals, marks):
    if marks == None:
        marks = []
    marks.append(getMarker())

    return marks

if __name__ == '__main__':
    app.run_server()