import requests

ORION_BASE_ADDRESS = 'http://127.0.0.1:1026/v2/'

def getAllFromCategory(category=""):
	productIds = []

	if category != "":
		url = ORION_BASE_ADDRESS + "entities?q=categoria=='"+category+"'"
		response = requests.get(url)

		for product in response.json():
			productIds.append(product['id'])
		
	return productIds