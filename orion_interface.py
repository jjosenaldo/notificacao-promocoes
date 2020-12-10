import requests

ORION_BASE_ADDRESS = 'http://127.0.0.1:1026/v2/'

class Product:
	def __init__(self, id, lat, lon, description, price, onSale, category, store):
		self.id = id 
		self.lat = lat
		self.lon = lon
		self.description = description
		self.price = price
		self.onSale = onSale
		self.category = category
		self.store = store


def getAllFromCategory(category=""):
	products = []

	if category != "":
		url = ORION_BASE_ADDRESS + "entities?q=categoria=='"+category+"'"
		response = requests.get(url)

		for productJson in response.json():
			product = Product(id=productJson['id'], lat=productJson['latitude'], lon=productJson['longitude'], description=productJson['descricao'], price=productJson['preco'], onSale=productJson['emPromocao'], category=productJson['categoria'], store=productJson['loja'] )
			products.append(product)
		
	return products