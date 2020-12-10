import requests
from server import HOST,PORT

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

def subscribeAll(products=[]):
	subscriptionIds = []

	for product in products:
		url = ORION_BASE_ADDRESS + 'subscriptions/'
		entities = [{'id':product.id, 'type':'Produto'}]
		subject = {'entities':entities, 'condition':{'attrs':['emPromocao']}}
		notification = {'http':{'url':'http://'+HOST+':'+str(PORT)}, 'attrs':[]}
		throttling = 5

		payload = {'subject':subject, 'notification':notification, 'throttling':throttling}
		response = requests.post(url, json=payload)

		subscriptionId = response.headers['Location'].split('/')[3]
		subscriptionIds.append(subscriptionId)

	return subscriptionIds

def unsubscribe(subscriptionId=""):
	if subscriptionId != "":
		url = ORION_BASE_ADDRESS + 'subscriptions/' + subscriptionId
		requests.delete(url)