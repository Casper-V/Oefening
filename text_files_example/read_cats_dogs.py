from count_words import woorden_tellen as w_t
from count_words import unieke_woorden_tellen as u_w_t

bestanden = ['cats.txt', 'dogs.txt', 'lizards.txt']
Emma = 'Emma_Austen.txt'

# for bestand in bestanden:
# 	try:
# 		with open(bestand) as f:
# 			tekst = f.read()
# 			print(tekst)
# 			w_t(bestand)
# 	except FileNotFoundError: 
# 		pass

with open(Emma, encoding='utf-8') as f:
	u_w_t(Emma, 'very')
