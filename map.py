import dash_leaflet as dl
from random import uniform as rand

def getMap(id='map', center=(-5.811967825768887, -34.20487439621176), zoom=7):
	return dl.Map(
        center=center, 
        zoom=zoom, 
        children=[dl.TileLayer(), dl.LayerGroup(children=[],id="layer")],
        id=id
    )

class Markers:
    def __init__(self):
        # Mapa do tipo < productId, Marker >
        self.markers = {}

    def addMarker(self, productId, marker):
        self.markers[productId] = marker

    def deleteMarker(self, productId):
        del self.markers[productId]

    def deleteAll(self):
        self.markers.clear()

    def getAllMarkers(self):
        return list(self.markers.values())

def createMarker(lat, lon):
    position = [lat, lon]

    return dl.Marker(position=position, children=dl.Tooltip("({:.3f}, {:.3f})".format(*position)))