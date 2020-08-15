# car = ['Audi', 'citroën', 'Volvo']
# car_lower = []
# for auto in car:
#     auto = auto.lower()
#     car_lower.append(auto)
# if 'audi' in car_lower:
#     print('Autootje')

# age_0 = 20
# age_1 = 14
# if (age_0 >= 18) and (age_1 >=18):
#     print('Welcome')
# else:
    # print('Sorry, not allowed')

# menu = ('brood', 'wijn', 'pizza', 'spaghetti', 'ijs')
# gerecht = 'biertje'
# if gerecht not in menu:
# 	print('Dit gerecht is op.')
# if 'brood' in menu:
# 	print('Dit is waar.')
# print('brood' in menu)
# if 'ijsje' in menu:
# 	print('Dit is niet waar.')
# print('ijsje' in menu)
# if 'ijsje' not in menu:
# 	print('Dit is waar.')
# print('ijsje' not in menu)

# cijferlijst = [7.0, 7.7, 8.1, 5.5, 3.6]
# geslaagd = []
# for cijfer in cijferlijst:
#     if cijfer >= 5.5:
#         geslaagd.append(cijfer)
# print(f"De cijfers zijn {geslaagd}")

# alien_color = 'gold'
# points = 0
# if alien_color == 'green':
#     bonus = 5
#     points += bonus
#     print(f"Je hebt {bonus} punten verdiend. Je hebt nu {points} punten.")
# elif alien_color == 'gold':
#     bonus = 15
#     points += bonus
#     print(f"Je hebt {bonus} punten verdiend. Je hebt {points} punten.")
# elif alien_color == 'red':
#     print(f"Deze alien levert geen punten op. Je hebt nu {points} punten.")
# else:
#     bonus = 10
#     points += bonus
#     print(f"Je hebt {bonus} punten verdiend. Je hebt nu {points} punten.")

# age = 70

# if age < 2:
#     print("Je bent een baby.")
# elif age < 4:
#     print("Je bent een peuter.")
# elif age < 13:
#     print("Je bent een kind.")
# elif age < 20:
#     print("Je bent een puber.")
# elif age < 65:
#     print("Je bent een volwassene.")
# elif age >= 65:
#     print("Je bent een bejaarde.")

# ingrediënten = ['extra kaas', 'peper', 'paprika', 'zeevruchten']
# ingrediënten_gast2 = []
# if ingrediënten:
#     for ingrediënt in ingrediënten:
#         print(f"Je pizza wordt bereid met {ingrediënt}.")
# if ingrediënten_gast2:
#     for ingrediënt in ingrediënten:
#         print(f"Je pizza wordt bereid met {ingrediënt}.")
# else:
#     print("Hoef je echt geen extra ingrediënten op je pizza?")

# username = ['admin', 'harry', 'hermione', 'ron', 'neville']
# # username = []
# if username:
#     for name in username:
#         if name == 'admin':
#             print(f"Welkom, {name}.")
#         else:
#             print(f"Leuk je te zien, {name}!")
# else:
#     print("Geef een gebruikersnaam op.")

current_users = ['admin', 'harry', 'hermione', 'Ron', 'neville']
current_users = [user.lower() for user in current_users]
new_users = ['lucius', 'Severus', 'albus', 'Harry', 'ron']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"De gebruikersnaam \'{new_user}\' bestaat al.")
    elif new_user.lower() not in current_users:
        print(f"Welkom, {new_user}!")
        print("Andere manier om je welkom te heten, %s" % (new_user))

lijst = list(range(1,10))
for cijfer in lijst:
    if cijfer == 1:
        print(f"{cijfer}st")
    elif cijfer == 2:
        print(f"{cijfer}nd")
    elif cijfer == 3:
        print(f"{cijfer}rd")
    else:
        print(f"{cijfer}th")