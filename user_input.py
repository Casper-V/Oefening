# vraag bij restaurant of er plek is
number_of_seats = int(input("How many seats do you want to reserve? "))
if number_of_seats <= 8:
    print (f"No problem. We have a table for {number_of_seats} seats ready for you.")
else:
    print ("Sorry, you will have to wait.")
