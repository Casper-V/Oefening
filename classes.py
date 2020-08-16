# class Hond:
# 	"""Eenvoudige representatie van een hond aan de hand van de naam,
# 	leeftijd en trucjes"""

# 	def __init__(self, naam_dier, leeftijd_dier):
# 		"""parameters naam en leeftijd toekennen aan de attributen name en age"""
# 		self.naam = naam_dier
# 		self.leeftijd = leeftijd_dier

# 	def zit(self):
# 		"""beschrijving van het trucje zit! dat de hond kan doen"""
# 		print(f"{self.naam.title()} is gaan zitten.")

# 	def lig(self):
# 		"""beschrijving van het trucje lig! dat de hond kan doen"""
# 		print(f"{self.naam.title()} is gaan liggen.")

# jouw_hond = Hond('Buffel', 2)
# print(f"Jouw hond heet {jouw_hond.naam} en is {jouw_hond.leeftijd} jaar oud.")
# jouw_hond.lig()

# mijn_hond = Hond('Blafbak', 14)
# print(f"Mijn hond heet {mijn_hond.naam} en is {mijn_hond.leeftijd} jaar oud.")
# mijn_hond.zit()

# class Restaurant:
# 	"""representatie van een restaurant"""
	
# 	def __init__(self, restaurant_name, cuisine_type):
# 		"""definieert een naam en type keuken"""	
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type

# 	def describe_restaurant(self):
# 		"""print de naam en het type keuken"""
# 		print(f"This restaurant is called \'{self.restaurant_name}\' and serves {self.cuisine_type}.")

# 	def open_restaurant(self):
# 		"""Kan worden aangeroepen om te printen dat het restaurant open is."""
# 		print(f"{self.restaurant_name} is open.")

# restaurant = Restaurant('Burger Earl', 'fastfood')
# # print(f"It\'s called {restaurant.restaurant_name}.")
# # print(f"They serve {restaurant.cuisine_type}.")
# # restaurant.describe_restaurant()
# # restaurant.open_restaurant()
# restaurant2 = Restaurant('Spinachio', 'vegetarian')
# restaurant3 = Restaurant('The Rib Giant', 'spareribs')
# restaurant.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()

class User:
	"""Kenmerken van een gebruiker"""

	def __init__(self, firstname, lastname, age, sex):
		"""Initialize a specific user"""
		self.firstname = firstname
		self.lastname = lastname
		self.age = age
		self.sex = sex

	def user_description(self):
		"""if called, provides basic info about the user"""
		print(f"Name: {self.firstname.title()} {self.lastname.title()}")
		print(f"Age: {self.age}")
		print(f"Sex: {self.sex}")

	def admin_rights(self):
		"""if called, prints the user has admin rights"""
		print(f"{self.firstname.title()} {self.lastname.title()} has admin rights.")

	def banned(self):
		"""if called, prints that the user is banned"""
		print(f"{self.firstname.title()} {self.lastname.title()} has been banned.")

user01 = User('fanny', 'pack', 22, 'female')
user01.user_description()
user01.admin_rights()

user02 = User('regina', 'reeves', 34, 'female')
user02.banned()
