from notifications import createNotification

class Buffer:
	def __init__(self):
		self.notfs = []

	def push(self, nome, preco, descricao):
		self.notfs.append(createNotification(nome, preco, descricao))

	def pop(self):
		tmp = self.notfs
		self.notfs=[]
		return tmp