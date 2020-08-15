# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# alien_0['x-position'] = 0
# alien_0['y-position'] = 25
# alien_0['speed'] = 'slow'
# alien_0['weapon'] = 'lasergun'

# if alien_0['speed'] == 'slow':
#     x_movement = 5
# elif alien_0['speed'] == 'medium':
#     x_movement = 10
# elif alien_0['speed'] == 'fast':
#     x_movement = 15

# # de alien beweegt x_movement naar rechts over de x-as
# alien_0['x-position'] += x_movement
# # print(alien_0)
# # del alien_0['weapon']

# # alien_weapon = alien_0['weapon']
# alien_weapon = alien_0.get('weapon', 'No weapon found.')

# print(alien_weapon)

# all_users = ['bob', 'harry', 'mary', 'boris', 'barry', 'cynthia', 'merol']
# names_in_dictionary = ['bob', 'barry', 'cynthia', 'merol']
# languages_to_select = ['python','c++', 'java', 'ruby', 'c#', 'php']
# favorite_languages = {
#     names_in_dictionary[0]: [languages_to_select[0], languages_to_select[3]],
#     names_in_dictionary[1]: [languages_to_select[1], languages_to_select[3]],
#     names_in_dictionary[2]: [languages_to_select[2]],
#     names_in_dictionary[3]: [],
#     }

# for name, languages in favorite_languages.items():
#     if len(languages) > 1:
#         print(f"{name.title()}'s favorite languages are: ")
#     elif len(languages) == 1:
#         print(f"{name.title()}'s favorite language is: ")
#     elif len(languages) == 0:
#         print(f"{name.title()} has no favorite language.")
#     for language in languages:
#         print(language.title())


# for name in all_users:
#     if name in favorite_languages.keys():
#         print(f"Dear {name.title()}, thanks for taking this poll.")
#     else:
#         print(f"Dear {name.title()}, please take the poll.")



# for oelekeboeleke in favorite_languages:
#     print (oelekeboeleke.title())
# if 'bob' in favorite_languages.keys():
#     print(f"Je bent helemaal geweldig!")
# for programming_language in favorite_languages.values():
#     print(programming_language)
# total_set = set(favorite_languages.values())
# print(total_set)

# # for fav in favorite_languages:
# #     print(f"{fav.title()}\'s favorite coding language is {favorite_languages[fav].title()}.")

# user = {
#     'first_name': 'anna',
#     'last_name': 'smith',
#     'age': 33,
#     'city_of_residence': 'Seattle'
#     }
# print(user['first_name'], user['last_name'])

# favorite_number = {'anna': 7, 'kelly': 7, 'john': 12, 'emerett': 42}
# favorite = favorite_number['anna']
# print(f"Anna's favorite number is {favorite}.")

# commands = {
#     'del': 'delete key and value permanently',
#     '.get()': 'get the value if the key exists, and return a default if it doesn\'t',
#     }

# commands['key'] = 'sleutel'
# commands['value'] = 'waarde'

# for k, v in commands.items():
#     print (f"Term: {k}\nDescription: {v}\n")

# command = 'del'
# print(commands['del'])
# command = '.get()'
# print(commands['.get()'])

# rivers = {'maas': 'nederland', 'rijn': 'duitsland', 'rhone': 'frankrijk', 'rio': 'brazilië'}
# for river, country in rivers.items():
#     print(f"De {river.title()} loopt door {country.title()}.")
# for river in rivers.keys():
#     print(river.title())
# for country in rivers.values():
#     print(country.title())

# aliens = []
# for alien in range(20):
#     alien = {'color':'green', 'points':5, 'speed':5, 'weapon':'lasergun'}
#     aliens.append(alien)

# for alien in aliens[:11]:
#     if alien['color'] == 'green':
#         alien['color'] = 'blue'
#         alien['points'] = 25
#         alien['speed'] = 20
#         alien['weapon'] = 'lasersword'

# print(aliens)

# pizza = {
#     'toppings': ['mushroom', 'gorgonzola'],
#     'crusts': ['thick', 'extra large'],
# }
# dough = []
# for crust in pizza['crusts']:
#     dough.append(crust)
# print(dough)

# print(f"You have ordered a pizza with a {dough[0]}, {dough[1]}"
#     " crust and the following toppings:")
# for topping in pizza['toppings']:
#     print(f"\t{topping}")

# artist = {
#     'bob dylan': {'age': 79, 'debut album': 1962, 'sex': 'male'},
#     'bruce springsteen': {'age': 71, 'debut album': 1973, 'sex': 'male'},
#     'nancy sinatra':  {'age': 80, 'debut album': 1962, 'sex': 'female'},
#     }

# for name, info in artist.items():
#     age = info['age']
#     debut_album = info['debut album']
#     sex = info['sex']
#     if sex == 'male':
#         print(f"{name.title()} is {age} years old. His first album was released in {debut_album}.")
#     elif sex == 'female':
#         print(f"{name.title()} is {age} years old. Her first album was released in {debut_album}.")

# friends = {
#     'friend_01': {
#                 'first_name': 'john',
#                 'last_name': 'travolta',
#                 'occupation': 'actor',
#                 'sex': 'male',
#                 },
#     'friend_02': {
#                 'first_name': 'bob',
#                 'last_name': 'dylan',
#                 'occupation': 'songwriter',              
#                 'sex': 'male',
#                 },
#     'friend_03': {
#                 'first_name': 'pat',
#                 'last_name': 'barker',
#                 'occupation': 'author',              
#                 'sex': 'female',
#                 },
#     }

# for friend, info in friends.items():
#     full_name = str(info['first_name']) + ' ' + str(info['last_name'])
#     occupation = info['occupation']
#     sex = info['sex']
#     if sex == 'male':
#         print(f"{full_name.title()} is a famous {occupation}. Isn't he great?")
#     if sex == 'female':
#         print(f"{full_name.title()} is a famous {occupation}. Isn't she great?")

# pets = []
# pet = {'name': 'fluffy', 'animal_type': 'bunny'}
# pets.append(pet)
# pet = {'name': 'cowboy', 'animal_type': 'bull'}
# pets.append(pet)
# pet = {'name': 'buffy', 'animal_type': 'butterfly'}
# pets.append(pet)

# for pet in pets:
#     print(f"This animal is called {pet['name'].title()}. It's a {pet['animal_type']}.")

# places = {
#     'john': ['london', 'paris', 'flevopolder'],
#     'sarah': ['london', 'amsterdam', 'rocky mountains'],
#     'dirk': ['volendam'],
#         }
# for name, cities in places.items():
#     cities_string = ', '.join(cities)
#     if len(cities) > 1:
#         print(f"{name.title()}'s favorite destinations are: {cities_string.title()}")
#     if len(cities) == 1:
#         print(f"{name.title()}'s favorite destination is: {cities_string.title()}")
#     for city in cities:
#         print(f"- {city.title()}")

# favorite_numbers = {'anna': [7, 23, 42],
#                     'kelly': [7, 1],
#                     'john': [12],
#                     'emerett': [],
#                     }
# for name, numbers in favorite_numbers.items():
#     if len(numbers) == 0:
#         print(f"{name.title()} has no favorite number.")
#     elif len(numbers) == 1:
#         print(f"{name.title()}\'s favorite number is:")
#         for number in numbers:
#             print(f"\t{number}")
#     else:
#         print(f"{name.title()}\'s favorite numbers are:")
#         for number in numbers:
#             print(f"\t{number}")
        
cities = {'london': {'population': 8_600_000, 'capital_of': 'United Kingdom'},
        'paris': {'population': 2_200_000, 'capital_of': 'France'},
        'amsterdam': {'population': 800_000, 'capital_of': 'The Netherlands'},
         }
for city, info in cities.items():
    print(f"The capital of {info['capital_of'].title()} is {city.title()}. It has a population of {info['population']}.")

cities = {'london': {'population': 8_600_000, 'capital_of': 'United Kingdom'},
        'paris': {'population': 2_200_000, 'capital_of': 'France'},
        'amsterdam': {'population': 800_000, 'capital_of': 'The Netherlands'},
         }
for city, info in cities.items():
    population = info['population']
    capital_of = info['capital_of']
    print(f"The capital of {info['capital_of'].title()} is {city.title()}. It has a population of {info['population']}.")