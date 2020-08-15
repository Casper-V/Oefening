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
#     album_info = {"Artist":artist, "Album title":album_title, "Number of tracks":n_tracks}
#     print(album_info)

# album_list = [["Bob Dylan", "Greatest Hits", 19], ["John Travolta", "Mix Tapes", 4], ["Guns N Roses", "Paradise City", 2]]
# for album in album_list:
#         make_album(album[0],album[1],album[2])

def begroet_gast(namen):
    for naam in namen:
        print(f"Welkom, {naam.title()}!")

gastenlijst = ['boris', 'fanny', 'jimmy', 'alexander']
begroet_gast(gastenlijst)