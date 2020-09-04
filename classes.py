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
		self.login_attempts = 0

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

	def increment_login_attempts(self):
		"""can be called upon a failed login attempt"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""resets the number of login attempts to 0"""
		self.login_attempts = 0
		print("Number of login attempts has been reset to 0.")

class Admin(User):
	"""Example of a kind of user that inherits from the parent class"""
	def __init__(self, firstname, lastname, age, sex):
		"""make an instance of an admin user"""
		super().__init__(firstname, lastname, age, sex)
		self.permissions = []

	def admin_permissions(self):
		"""list which permissions an admin user has
		This method requires input in the form of:
		user01.permissions = ['can edit posts', etc.]
		user01.admin_permissions()"""
		print(f"{self.firstname.title()} {self.lastname.title()} is an admin user with the following permissions:")
		for permission in self.permissions:
			print(f"- {permission}")

# user01 = User('fanny', 'pack', 22, 'female')
user01 = Admin('fanny', 'pack', 22, 'female')
user01.user_description()
user01.admin_rights()
user01.permissions = [
	'can edit posts',
	'can delete posts',
	'can ban users',
	'can lock threads',
]
user01.admin_permissions()

#three login attempts
user01.increment_login_attempts()
user01.increment_login_attempts()
user01.increment_login_attempts()
print(f"Total number of login attempts: {user01.login_attempts}")
#resetting the counter
user01.reset_login_attempts()
print(f"Total number of login attempts: {user01.login_attempts}")

print("")
user02 = User('regina', 'reeves', 34, 'female')
user02.banned()

# just a line break for clarity
print()

#Alternatieve schrijfwijze van onderstaande class Fiets
# class Fiets:
# 	"""representatie van verschillende modellen fietsen"""
# 	def __init__(self, merk, model, bouwjaar):
# 		"""instantie maken van fiets"""
# 		"""th staat voor tweedehands"""
# 		self.merk = merk
# 		self.model = model
# 		self.bouwjaar = bouwjaar

# 	def beschrijving_fiets(self):
# 		""""retourneert" een beschrijving van de fiets"""
# 		beschrijving = f"Merk = {self.merk}. Model = {self.model}. Bouwjaar = {self.bouwjaar}."
# 		return beschrijving;

# 	def tweedehands(self, th):
# 		"""indien aangeroepen: geeft aan dat de fiets tweedehands is"""
# 		if th == True:
# 			print("Deze fiets is tweedehands.")
# 		else:
# 			print("Deze fiets is nieuw.")

# mijn_fiets = Fiets("Gazelle", "BB4", 1999)
# print(mijn_fiets.beschrijving_fiets())
# mijn_fiets.tweedehands(True)
# mijn_fiets = Fiets("Batavus", "ElectroMagic", 2018)
# print(mijn_fiets.beschrijving_fiets())
# mijn_fiets.tweedehands(False)

class Fiets:
	"""representatie van verschillende modellen fietsen"""
	def __init__(self, merk, model, bouwjaar, th):
		"""instantie maken van fiets
		th staat voor tweedehands
		prijs is hier een optionele parameter met standaardwaarde 0""" 
		self.merk = merk
		self.model = model
		self.bouwjaar = bouwjaar
		self.th = th
		self.prijs = 0

	def beschrijving_fiets(self):
		""""retourneert" een beschrijving van de fiets"""
		beschrijving = f"Merk = {self.merk}. Model = {self.model}. Bouwjaar = {self.bouwjaar}."
		return beschrijving;

	def tweedehands(self):
		"""indien aangeroepen: geeft aan dat de fiets tweedehands is"""
		if self.th == True:
			print("Deze fiets is tweedehands.")
		else:
			print("Deze fiets is nieuw.")

	def huidige_prijs(self):
		"""prijs instellen door een prijs in te voeren via de variabele mijn_fiets.prijs = 250"""
		if self.prijs <= 0:
			print("Er is nog geen prijs ingesteld voor deze fiets.")
		else:
			print(f"Deze fiets kost {self.prijs}.")

	def verkoopprijs(self, verkoopprijs):
		"""alternatief voor huidige_prijs():
		prijs instellen door een prijs in te voeren via de methode mijn_fiets.verkoopprijs(2500)"""
		self.prijs = verkoopprijs
		self.huidige_prijs()

	def prijsaanpassing(self, prijsverhoging):
		"""kan worden aangeroepen om een nieuwe prijs door te geven
		als de oorspronkelijke prijs bewaard moet blijven"""
		self.prijs += prijsverhoging
		print("Let op! De prijs van deze fiets is gewijzigd.")
		self.huidige_prijs()

mijn_fiets = Fiets("Gazelle", "BB4", 1999, True)
print(mijn_fiets.beschrijving_fiets())
mijn_fiets.tweedehands()
mijn_fiets.prijs = 250
mijn_fiets.huidige_prijs()

mijn_fiets = Fiets("Batavus", "ElectroMagic", 2018, False)
print(mijn_fiets.beschrijving_fiets())
mijn_fiets.tweedehands()
# mijn_fiets.huidige_prijs()
mijn_fiets.verkoopprijs(2500)
mijn_fiets.prijsaanpassing(400)

