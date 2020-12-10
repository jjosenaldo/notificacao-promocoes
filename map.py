import dash_leaflet as dl
from random import uniform as rand

def getMap(id='map-promocoes', center=(-5.811967825768887, -34.20487439621176), zoom=7):
	return dl.Map(
        center=center, 
        zoom=zoom, 
        children=[dl.TileLayer(), dl.LayerGroup(children=[],id="layer")],
        id=id, 
        style={
            'width': '50%', 
            'height': '100%', 
            'margin': "0", 
            "display": "block"
        }
    )

def getMarker(position=None):
    if position == None:
        lat = -5.811967825768887
        lon = -34.20487439621176
        eps = 0.5
        position = [rand(lat-eps, lat+eps), rand(lon-eps, lon+eps)]

    return dl.Marker(position=position, children=dl.Tooltip("({:.3f}, {:.3f})".format(*position)))

getMarker()