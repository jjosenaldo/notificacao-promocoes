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
        # Mapa do tipo < subscriptionId, Marker >
        self.markers = {}

    def addMarker(self, subscriptionId, marker):
        self.markers[subscriptionId] = marker

    def deleteMarker(self, subscriptionId):
        del self.markers[subscriptionId]

    def getAllMarkers(self):
        return list(self.markers.values())

def createMarker(lat, lon):
    position = [lat, lon]

    return dl.Marker(position=position, children=dl.Tooltip("({:.3f}, {:.3f})".format(*position)))

createMarker(10,10)