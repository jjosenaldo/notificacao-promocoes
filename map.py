import dash_leaflet as dl

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