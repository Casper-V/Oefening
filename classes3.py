"""module to practice importing other modules"""
from classes2 import User, Admin
from classes_restaurant import Restaurant, HighlightedRestaurant, CustomerCheers, IceCreamParlor

user20 = User("John", "Lemon", 45, "male")
user21 = User("Bob", "Hobo", 18, "male")
user20.user_description()
user21.user_description()

restaurant20 = Restaurant("Duck 4 ever", "roasted duck")
restaurant20.describe_restaurant()