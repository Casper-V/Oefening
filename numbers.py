from random import randint, choice

# x = 4_000_000
# # tot_de_derde = x ** 3
# helft = x/2
# # print(tot_de_derde)
# print(helft)

# x,y = 4,5
# print(x**y)


willekeurig = randint(1,10)
favoriet = 9
if favoriet < willekeurig:
	print(f"Je favoriete getal is kleiner dan {willekeurig}")
elif favoriet > willekeurig:
	print(f"Je favoriete getal is groter dan {willekeurig}")
controle = f"Je favoriete getal is {favoriet}"
print(controle)

kanshebbers = ["Bob", "Tina", "Bert", "Ernie", "Pino"]
loterijwinnaar = choice(kanshebbers)
print(loterijwinnaar)
# import this