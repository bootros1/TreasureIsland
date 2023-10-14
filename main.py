

print("Welcome to Treasure Island. Your mission is to find the treasure.")
print("You will need to make a choice when playing this game.")

# this is to indicate if you want to go to the left or right.
choice1= input('Please choose one of the choices, "left" or right: ')
if choice1.lower() == 'right':
    print("Game Over")
    choice2 = input('You will need to choose whether you want to "swim" or "wait" ')
    # option 2, you get to choose swim or wait.
    if choice2.lower() == 'swim':
        print("Game over")
        # This last option decides if you win the game or not.
        door_selection = input("Now it is time to choose your door color, yellow, blue or red: ")
        if door_selection.lower() == 'red':
            print("Game over")
        elif door_selection.lower() == 'blue':
            print("Game over")
        else:
            print("You win!")
    else:
        print("proceed to next level.")

else:
    print("You can proceed.")


print("Thank you for playing this game.")