# magicians = [(]'hans kazan', 'david copperfield', 'donald duck']
# for magician in magicians:
# 	print(f"Mooie truc, {magician.title()}!")

# pizza_s = ['quattro stagioni', 'margarita', 'frutti de mer']
# for pizza in pizza_s:
# 	print(f"Ik heb zin in een {pizza.title()}...")
# print("Ik houd van kaas.\nIk houd van tomaat.\nIk houd van deeg.\nDus ook van pizza!")

# dubbel = []
# for cijfer in range(10,20,2):
# 	verdubbeld = cijfer*2
# 	dubbel.append(verdubbeld)
# print(dubbel)
# # hetzelfde met andere code
# dubbele_cijfers = [cijfer*2 for cijfer in range(10,20,2)]
# print(dubbele_cijfers)

# numbers = []
# for number in range(1,101,2):
# 	numbers.append(number)
# 	print(number)
# 	print(sum(numbers))

# kubus = []
# for cijfer in range(1,11):
# 	cijfer **= 3
# 	kubus.append(cijfer)
# print(kubus)

kubus = [cijfer**3 for cijfer in range(1,11)]
hoekje = kubus[-3:]
print(kubus)
print(hoekje)
kopie_kubus = kubus[:]
print(kopie_kubus)


# drieën = [cijfer*3 for cijfer in range(3,31,3)]
# print(drieën)


# for cijfer in range(20):
# 	print(cijfer)

# cijfers = list(range(10,20,2))
# print(cijfers)