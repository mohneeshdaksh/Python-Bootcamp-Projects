'''Treasure Island'''
print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure!!!")
direction = (input("Which direction would you like to go? Left or Right? ")).lower()
if direction == "left":
    swim_wait = (input("Do you want to swim or wait? ")).lower()
    if swim_wait == "wait":
        door = (input("Choose a door! Blue, Red or Yellow? ")).lower()
        if door == "yellow":
            print("You won!!!")
        elif door == "red":
            print("Burned by fire. Game Over!")
        elif door == "blue":
            print("Eaten by beasts. Game Over!")
        else:
            print("Game Over!")
    else:
        print("Attacted by trout. Game Over!")
else:
    print("Fall into a hole. Game Over!")
