'''Python Pizza Deliveries'''

print("Thank you for choosing Python Pizza Deliveries!")

size = input("Which size of pizza would you like to have? S, M or L? ")
add_pepperoni = input("Do you want pepperoni on it? Y or N? ")
extra_cheese = input("Would you like to have an extra cheese on your pizza? Y or N? ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid entry! :(")
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
else:
    pass
print(f"Your final bill is: ${bill}.")
