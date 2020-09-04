from random import randint, choice

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
			'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
winnende_nummers = []

class LetterGetal():
	"""class om een willekeurig getal of letter te selecteren"""
	def __init__(self, aantal_cijfers, aantal_letters):
		self.aantal_letters = aantal_letters
		self.aantal_cijfers = aantal_cijfers

	def willekeurig_resultaat(self):
		for cijfer in range(0, self.aantal_cijfers):
			getrokken_cijfer = randint(1,10)
			winnende_nummers.append(getrokken_cijfer)
		for letter in range(0, self.aantal_letters):
			getrokken_letter = choice(letters)
			winnende_nummers.append(getrokken_letter)
		
trekking01 = LetterGetal(2, 2)
trekking01.willekeurig_resultaat()
print(winnende_nummers)

# hieronder zonder class

letters_en_cijfers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
te_trekken_aantal = 4

while len(winnende_nummers) < te_trekken_aantal:
	getrokken = choice(letters_en_cijfers)
	if getrokken not in winnende_nummers:
		# print(f"We hebben een {getrokken}!")
		winnende_nummers.append(getrokken)
print(f"De winnende nummers zijn: {winnende_nummers}")
