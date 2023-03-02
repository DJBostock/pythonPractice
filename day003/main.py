print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First Choice
print("You come to a crossroad. Where do you want to go?")
choice_1 = (input("Type \"left\" or \"right\" to choose.")).lower()
if choice_1[0] != "l":
    print("You get lost in the woods and are eaten by a bear. Game over.")
else:
    # Second Choice
    print("You come to a lake. There is an island in the middle of the lake.")
    choice_2 = (input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")).lower()
    if choice_2[0] != "w":
        print("You try to swim across. You are eaten by a crocodile. Game over.")
    else:
        # Third Choice
        print("You arrive at the island unharmed. There is a house with three doors.")
        choice_3 = (input("Do you choose the \"red\" door, the \"blue\" door, or the \"green\" door?")).lower()
        if choice_3[0] == "r":
            print("You are engulfed in fire. Game over.")
        elif choice_3[0] == "b":
            print("A tiger leaps out and gobbles you up. Game over.")
        else:
            print("You find a chest full of treasure. You win. Game over.")
