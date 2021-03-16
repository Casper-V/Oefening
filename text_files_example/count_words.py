def woorden_tellen(bestandsnaam):
    """Maakt een schatting van het aantal woorden in een tekstbestand"""
    try:
        with open(bestandsnaam, encoding='utf-8') as f:
            content = f.read()
    except:
        print("Bestand niet gevonden!")
    else:
        file_as_list = content.split()
        number_of_words = len(file_as_list)
        print(f"{bestandsnaam} bevat {number_of_words} woorden.")

def unieke_woorden_tellen(bestandsnaam, woord):
    """Telt hoe vaak een opgegeven woord in de tekst voorkomt."""
    try:
        with open(bestandsnaam, encoding='utf-8') as f:
            content = f.read()
            aantal_keer = content.count(woord.lower())
            print(f"Het woord \'{woord}\' komt {aantal_keer} keer voor in {bestandsnaam}.")
    except:
        print("Bestand niet gevonden!")



# # voorbeeld1
# bestandsnaam = 'python_text.txt'
# woorden_tellen(bestandsnaam)

# # voorbeeld2
# meerdere_bestanden = ['python_text.txt', 'text_example.txt', 'this_file_doesnt_exist.txt']
# for bestand in meerdere_bestanden:
#     woorden_tellen(bestand)