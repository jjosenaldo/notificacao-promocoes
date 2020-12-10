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
subscriptionIds = []

# ------------------------------ Server config -----------------------------

server = Flask(__name__)    

# @server.route('/notify', methods=['POST'])
# def home():
#     products = []
#     try:
#         for onSale in request.json['contextResponses']:
#             product = {}
#             for attrib in onSale['contextElement']['attributes']:
#                 product[attrib['name']] = attrib['value']
#             product['nome'] = product['descricao']

#             buf.push(product['nome'],product['preco'],product['descricao'])

#             products.append(product)
#         return Response(status=200)
#     except KeyError:
#         return Response(status=400)

@server.route('/notify', methods=['POST'])
def home():
    productJson = request.json['data'][0]
    print(productJson)
    productId = productJson['id']
    lat = float(productJson['latitude']['value'])
    lon = float(productJson['longitude']['value'])

    if productJson['emPromocao']['value'] == "true":
        buf.push(productJson['descricao']['value'],productJson['preco']['value'],productJson['descricao']['value'])
        markers.addMarker(productId, createMarker(lat, lon))
        print("\n")
        print("ta em promo")
        print("\n")
    else:
        print("\n")
        print("nao ta em promo")
        print("\n")
        markers.deleteMarker(productId)
    

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
        products = getProductsFromCategory(value)
        showOnMapIfOnSale(products)

    raise PreventUpdate('')

def showOnMapIfOnSale(unfilteredProducts):
    updateMarkersFromProducts([prod for prod in unfilteredProducts if prod.onSale=="true"])

def updateMarkersFromProducts(products):
    global subscriptionIds
    unsubscribe(subscriptionIds)
    subscriptionIds = subscribeAll(products)
    markers.deleteAll()

    for product in products:
        marker = createMarker(product.lat, product.lon)
        markers.addMarker(product.id, marker)

def clearSelectedProcuts():
    global subscriptionIds
    unsubscribe(subscriptionIds)
    subscriptionIds = []
    markers.deleteAll()

# ------------------------------ Main --------------------------------------

if __name__ == '__main__':
    app.run_server(host=HOST, port=PORT)