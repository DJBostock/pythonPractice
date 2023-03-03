import random

print("Welcome to the game")

user_choice = int(input("Type \"0\" for rock, \"1\" for paper, or \"2\" for scissors: "))
computer_choice = random.randint(0, 2)

if user_choice == 0:
    print("You chose rock.")
    if computer_choice == 0:
        print("Computer chose rock. It's a draw.")
    elif computer_choice == 1:
        print("Computer chose paper. You lose.")
    else:
        print("Computer chose scissors. You win.")
elif user_choice == 1:
    print("You chose paper")
    if computer_choice == 0:
        print("Computer chose rock. You win.")
    elif computer_choice == 1:
        print("Computer chose paper. It's a draw.")
    else:
        print("Computer chose scissors. You lose.")
else:
    print("You chose scissors")
    if computer_choice == 0:
        print("Computer chose rock. You lose.")
    elif computer_choice == 1:
        print("Computer chose paper. You win.")
    else:
        print("Computer chose scissors. It's a draw.")
