class Restaurant:
	"""representatie van een restaurant"""
	
	def __init__(self, restaurant_name, cuisine_type):
		"""definieert een naam en type keuken"""	
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.guests = 0

	def describe_restaurant(self):
		"""print de naam en het type keuken"""
		print(f"This restaurant is called \'{self.restaurant_name}\' and serves {self.cuisine_type}.")

	def open_restaurant(self, open):
		"""Kan worden aangeroepen om te printen dat het restaurant open is."""
		if open == True:
			print(f"{self.restaurant_name} is open.")
		else:
			print(f"{self.restaurant_name} is closed.")

	def set_no_guests(self, guests):
		"""hiermee kan het aantal gasten worden opgegeven"""
		self.guests = guests

	def extra_guests(self, extra_guests):
		"""hiermee kan een toename/afname van het aantal gasten worden opgegeven"""
		self.guests += extra_guests

	def print_guests(self):
		"""aanroepen als het aantal gasten moet worden geprint
		Alternatief, zie hieronder buiten de class: print(f"Number of guests: {restaurant.guests}")"""
		if self.guests == 1:
			print(f"At the moment, there is only {self.guests} guest in {self.restaurant_name}.")
		elif self.guests == 0:
			print(f"At the moment, there are no guests in {self.restaurant_name}.")
		else:
			print(f"At the moment, there are {self.guests} guests in {self.restaurant_name}.")

class HighlightedRestaurant(Restaurant):
	"""Lets's assume that the restaurant can pay a fee to appear highlighted in the search results.
	This makes the restaurant a recommended (highlighted) restaurant.
	The more 'cheers' it has, the higher it is recommended."""
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.max_cheers = 10
		self.number_of_cheers = 0

	def recommendation(self, number_of_cheers):
		"""if called, prints a statement that this restaurant is recommended
		it can include a review score (number of cheers) from customers"""
		self.number_of_cheers = number_of_cheers
		if number_of_cheers <= 0 or number_of_cheers > 10:
			print(f"This restaurant comes highly recommended!")
		else:
			print(f"This restaurant comes highly recommended! We give this restaurant {self.number_of_cheers} out of {self.max_cheers} cheers!")
		self.customer_cheers = CustomerCheers()
		

	def describe_restaurant(self):
		"""overgenomen en aangepast van de parent class Restaurant.
		Description is more elegant to make the restaurant stand out."""
		print(f"\'{self.restaurant_name}\' is a fantastic restaurant for all you foodies out there! "
			f"{self.restaurant_name} serves some of the best {self.cuisine_type} in town. "
			"You won't be disappointed!")

class CustomerCheers:
	"""Define a number of cheers (review score) given by customers on a scale of 1-10.
	The review score is only included for highlighted restaurants.
	This is just used as an example of using instances as attributes, it might not make much sense."""
	def __init__(self, customer_cheers = 7):
		self.customer_cheers = customer_cheers
		
	def print_customer_cheers(self, customer_cheers):
		self.customer_cheers = customer_cheers
		print(f"This restaurant receives {self.customer_cheers} cheers from their customers.")

class IceCreamParlor(Restaurant):
	"""subclass of Restaurant, used solely for ice cream parlors"""
	def __init__(self, restaurant_name, cuisine_type = "ice cream"):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = []

	"""call to print a list of ice cream flavors
	This method requires input in the form of:
	ice_parlor.flavor_menu(["strawberry", "chocolate", "cherry", "bananas", "oreo", "vanilla"])"""
	def flavor_menu(self, flavors):
		print(f"{self.restaurant_name} offers the following flavors:")
		for flavor in flavors:
			print(flavor)

ice_parlor = IceCreamParlor("Ice, Ice, Baby")
ice_parlor.describe_restaurant()
ice_parlor.open_restaurant(True)
ice_parlor.set_no_guests(4)
ice_parlor.print_guests()
ice_parlor.flavor_menu(["strawberry", "chocolate", "cherry", "bananas", "oreo", "vanilla"])

# restaurant = Restaurant('Burger Earl', 'fastfood')
# restaurant2 = Restaurant('Spinachio', 'vegetarian')
# restaurant3 = Restaurant('The Rib Giant', 'spareribs')
# #restaurant4 heeft de subklasse HighlightedRestaurant
# restaurant4 = HighlightedRestaurant('The Golden Spoon', 'French delicacies')

# restaurant.describe_restaurant()
# restaurant.open_restaurant(True)
# restaurant.set_no_guests(20)
# restaurant.extra_guests(35)
# restaurant.print_guests()
# # de regel hieronder is een andere manier om het aantal gasten op te halen, zonder de methode print_guests
# print(f"Number of guests: {restaurant.guests}")
# print("")
# restaurant2.describe_restaurant()
# restaurant2.open_restaurant(True)
# restaurant2.set_no_guests(6)
# restaurant2.extra_guests(-5)
# restaurant2.print_guests()
# print("")
# restaurant3.describe_restaurant()
# restaurant3.open_restaurant(False)
# restaurant3.print_guests()
# print("")
# restaurant4.describe_restaurant()
# restaurant4.recommendation(9)
# # next line calls the separate class CustomerCheers, which is included in
# # the highlightedRestaurant class as self.customer_cheers = CustomerCheers()
# restaurant4.customer_cheers.print_customer_cheers(8)
# restaurant4.open_restaurant(True)
# restaurant4.set_no_guests(14)
# restaurant4.print_guests()
# print("")



