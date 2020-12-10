#!/usr/bin/python3
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from flask import Flask, request, Response

import dropdown
import map
from map import *
from panels import createMainPanel
from server import HOST,PORT
from buffer import Buffer
from orion_interface import *

# ------------------------------ Globals -----------------------------------

markers = Markers()
buf = Buffer()

# ------------------------------ Server config -----------------------------

server = Flask(__name__)    

@server.route('/', methods=['POST'])
def home():
    products = []
    for onSale in request.json['contextResponses']:
        product = {}
        for attrib in onSale['contextElement']['attributes']:
            product[attrib['name']] = attrib['value']
        product['nome'] = product['descricao']

        buf.push(product['nome'],product['preco'],product['descricao'])

        products.append(product)
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
    Output("notifications", "children"),
    Input("interval-component", "n_intervals"),
    State("layer", "children"),
    State("notifications", "children"))
def map_update(n_intervals, marks, notfs):
	global markers
	return markers.getAllMarkers(), buf.pop()+notfs



@app.callback(
	Output('hidden-dropdown-div', 'style'),
    Input('dropdown-categorias', 'value'))
def on_dropdown_value_changed(value):
	if value == "" or value == None:
		clearSelectedProcuts()
	else:
		products = getAllFromCategory(value)
		updateMarkersFromProducts(products)

	raise PreventUpdate('')

def updateMarkersFromProducts(products):
	subscriptionIds = subscribeAll(products)
	markers.deleteAll()

	for product in products:
		marker = createMarker(product.lat, product.lon)
		markers.addMarker(product.id, marker)

def clearSelectedProcuts():
	subscriptionIds = []
	markers.deleteAll()

# ------------------------------ Main --------------------------------------

if __name__ == '__main__':
    app.run_server(host=HOST, port=PORT)