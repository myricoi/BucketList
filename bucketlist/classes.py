users = []
bucketlists = []


class User(object):
	"""
	This class is the model for a user. Instantiating the class
	creates a new user who is added to the list of users.
	"""
	def __init__(self, firstname, lastname, username, password, email):
		self.firstname = firstname
		self.lastname = lastname
		self.username = username
		self.password = password
		self.email = email
		users.append(self)

	def getLoginDetails(self):
		return [self.username, self.password]


class Bucketlist(object):

	def __init__(self, name, owner):
		self.owner = owner
		self.items = []
		self.name = name
		bucketlists.append(self)

	def addItem(self, item):
		self.items.append(item)

	def removeItem(self, item):
		for i in self.items:
			if(i == item):
				del self.items[self.items.index(i)]

	def getItems():
		return self.items

	def getOwner():
		return [self.owner.username, self.owner.password]
