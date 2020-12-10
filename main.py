#!/usr/bin/python3
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from flask import Flask, request, Response

import dropdown
import map
from map import Markers
from panels import createMainPanel
from server import HOST,PORT

# ------------------------------ Globals -----------------------------------

markers = Markers()

# ------------------------------ Server config -----------------------------

server = Flask(__name__)    

@server.route('/', methods=['POST'])
def home():
    callback(request.json)
    return Response(status=200)

# ------------------------------ Dash config -------------------------------

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
	global markers
	return markers.getAllMarkers()

@app.callback(
	Output('hidden-dropdown-div', 'style'),
    Input('dropdown-categorias', 'value'))
def on_dropdown_value_changed(value):
    print('You have selected "{}"'.format(value))
    raise PreventUpdate('')

# ------------------------------ Main --------------------------------------

if __name__ == '__main__':
    app.run_server(host=HOST, port=PORT)