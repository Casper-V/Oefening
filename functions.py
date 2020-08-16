# def functienaam():
#     """Tussen driedubele aanhalingstekens komt de docstring, die uitlegt wat de functie doet"""
#     print("Hier wordt de functie uitgevoerd")
# functienaam()

# gebruikers = ["Rickie", "Boris", "Donald"]

# def begroeting(naam):
#     """Iemand begroeten"""
#     print(f"Hallo, {naam.title()}!")

# for gebruiker in gebruikers:
#     begroeting(gebruiker)

# def favoriete_boek(titel="Titel", auteur="Schrijver"):
#     print(f"Mijn favoriete boek is {titel} van {auteur}.")
# favoriete_boek("The Ghost Road", "Pat Barker")
# favoriete_boek(titel="Guards! Guards!", auteur="Terry Pratchett")
# favoriete_boek("Titel")

# def make_shirt(size="M", Print="My favorite band"):
#     print(f"This is a size {size} shirt containing the print {Print}.")
# make_shirt()
# make_shirt("L", "Slayer")
# make_shirt(Print="Iron Maiden", size="XXL")

# def topografie(stad, land="nederland"):
#     print(f"{stad.title()} ligt in {land.title()}.")
# topografie("brussel", "belgië")
# topografie("utrecht")
# topografie(stad="zwolle")
# topografie(stad="mechelen", land='belgië')

def naam(voornaam='', achternaam='', tweede_voornaam=''):
    if tweede_voornaam:
        volledige_naam = f"{voornaam} {tweede_voornaam} {achternaam}"
    else: 
        volledige_naam = f"{voornaam} {achternaam}"
    return volledige_naam.title() 

# def naam_dict(voornaam='', achternaam='', tweede_voornaam=''):
#     if tweede_voornaam:
#         volledige_naam_dict = {'voornaam':voornaam, 'achternaam':achternaam, 'tweede_voornaam':tweede_voornaam}
#     else: 
#         volledige_naam_dict = {'voornaam':voornaam, 'achternaam':achternaam}
#     return volledige_naam_dict
# gebruiker0 = naam(voornaam='pief', achternaam='poef', tweede_voornaam='paf')
# gebruiker1 = naam("boris", "jeltzin")
# gebruiker0_dict = naam_dict(voornaam='pief', achternaam='poef', tweede_voornaam='paf')
# gebruiker1_dict = naam_dict("boris", "jeltzin")
# print(gebruiker0)
# print(gebruiker1)
# print(gebruiker0_dict)
# print(gebruiker1_dict)

# def credentials(username,password):
#     print(f"{username}\'s password is {password}.")

# while True:
#     print("You will be asked to enter your user name and password. You can press q to quit.")
#     user = input("Enter your user name: ")
#     passw = input("Enter your password: ")
#     credentials(user,passw)
#     if user == "q" or passw == "q":
#         break

# def topography(city,country):
#     print(f"{city.title()}, {country.title()}")

# topography("amsterdam", "netherlands")
# topography("brussels", "belgium")


# def make_album(artist, album_title, n_tracks):
#     """returns a dictionary containing one album and info on that album"""
#     album_info = {"Artist":artist, "Album title":album_title, "Number of tracks":n_tracks}
#     print(album_info)

# album_list = [["Bob Dylan", "Greatest Hits", 19], ["John Travolta", "Mix Tapes", 4], ["Guns N Roses", "Paradise City", 2]]
# for album in album_list:
#         make_album(album[0],album[1],album[2])


# def begroet_gast(namen):
#     """"prints a separate line of greeting for for each guest included in the inputed list"""
#     for naam in namen:
#         print(f"Welkom, {naam.title()}!")

# gastenlijst = ['boris', 'fanny', 'jimmy', 'alexander']
# begroet_gast(gastenlijst)


# def pizzas(ordered, ready_to_serve):
#     """Will move pizza orders from the ordered list to the ready_to_serve list
#     after instruction the kitchen which pizzas to make"""
#     while ordered:
#         current_pizza = ordered.pop()
#         ready_to_serve.append(current_pizza)
#         print(f"The customers has ordered a {current_pizza}.")

# def ready(ready_to_serve):
#     """"Will print an overview of the pizzas that are ready to serve"""
#     for pizza in ready_to_serve:
#         print(f"The following is ready to serve: {pizza}")

# ordered = ['margarita', 'quattro_staggioni', 'salami', 'seafood', 'pineapple']
# ready_to_serve = []

# pizzas(ordered[:], ready_to_serve)
# ready(ready_to_serve)
# print(ordered)

# Eerst wordt een willekeurige routebeschrijving weergegeven als lijst
# route = ['rechtdoor', 'rechtsaf', 'na 50 meter schuin naar links', 'bij het stoplicht rechtsaf', 'linksaf']

# def toon_richting(richtingen):
#     """"De eerste richtingaanwijzing van de route wordt apart beschreven.
#     Dan komen de resterende richtingaanwijzingen.
#     Tot slot een laatse aanwijzing."""
#     eerste_richtingaanwijzing = route[0]
#     overige_richtingaanwijzingen = route[1:-1]
#     laatste_richtingaanwijzing = route[-1]
#     print(f"Eerst ga je {eerste_richtingaanwijzing}.")
#     for richting in overige_richtingaanwijzingen:
#         print(f"Vervolgens ga je {richting}.")
#     print(f"Tot slot ga ja {laatste_richtingaanwijzing}. Je hebt je bestemming bereikt.")

# toon_richting(route)

# route2 = route[:]

# def broodje_beleggen(grootte, *broodbeleg):
#     print(broodbeleg)
#     print(f"Je hebt een {grootte} broodje besteld met:")
#     for beleg in broodbeleg:
#         print(f"- {beleg}")

# broodje_beleggen('middelgroot', 'zwitserse kaas', 'tomaat', 'roomboter')
# broodje_beleggen('klein', 'ei')

# def profiel_maken(voornaam, achternaam, **info):
#     """Een dictionary maken met alle info die over een gebruiker bekend is"""
#     info['voornaam'] = voornaam
#     info['achternaam'] =  achternaam
#     return info

# gebruikersprofiel1 = profiel_maken('tom', 'petty', occupation='musician', alive='no')
# gebruikersprofiel2 = profiel_maken('tom', 'cruise', occupation='actor', alive='yes', famous_for=['top gun', 'misscion impossible'])
# print(gebruikersprofiel1)
# print(gebruikersprofiel2)