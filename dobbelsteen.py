from random import randint

class Die():
    """representation of casting a die"""
    def __init__(self, sides):
        self.sides = sides

    def print_roll_die(self):
        """performs and prints the die roll and for clarity states what kind of die is used"""
        self.roll = randint(1, self.sides)
        print(f"This die has {self.sides} sides. You have rolled a {self.roll}")

    def no_print_roll_die(self):
        """perfoms the die roll and returns the value without printing it"""
        self.roll = randint(1, self.sides)
        return self.roll

# create two instances of dices
d6 = Die(6)
d20 = Die(20)

# roll both dice ten times and store the results in a list
ten_rolls = []
for roll in range(0,10):
    result = d6.no_print_roll_die()
    ten_rolls.append(result)
print(ten_rolls)
average = sum(ten_rolls) / len(ten_rolls)
print(f"Average result: {average}")

ten_rolls = []
for roll in range(0,10):
    result = d20.no_print_roll_die()
    ten_rolls.append(result)
print(ten_rolls)
average = sum(ten_rolls) / len(ten_rolls)
print(f"Average result: {average}")

# roll_number = 1
# # tien keer rollen met while-loop
# while roll_number < 11:
#     print(f"This is roll {roll_number}.")
#     d6.print_roll_die()
#     roll_number += 1
# print("-----------------------------")
# # tien keer rollen met range
# for roll in range(0,10):
#     d20.print_roll_die()
