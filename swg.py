import random


choice = ["snake","water","gun"]


print('''

            CHOICE
       
        [   SNAKE   ]
        [    GUN    ]
        [   WATER   ]
      
    TYPE EXIT FOR CLOSING GAME
''')

GameRun = True


def game(user_choice, computer_choice):
    if (user_choice == computer_choice):
        return "Draw"
    elif (user_choice == "exit"):
        return "Exit"
    elif ((computer_choice == "snake") and (user_choice =="gun")):
        return "YOU WIN"
    elif ((computer_choice == "water") and (user_choice == "snake")):
        return "YOU WIN"
    elif ((computer_choice == "gun") and (user_choice == "water")):
        return "YOU WIN"
    elif ((computer_choice == "snake") and (user_choice == "water")):
        return "COMPUTER WINS"
    elif ((computer_choice == "gun") and (user_choice == "snake")):
        return "COMPUTER WINS"
    elif ((computer_choice == "water") and (user_choice == "gun")):
        return "COMPUTER WINS"
    else:
        return " INVALID INPUT "

while GameRun :
    computer_choice = random.choice(choice)
    user_choice = input("Enter Your Choice : ")
    user_choice = user_choice.lower()

    result = game(user_choice , computer_choice )
    if ((user_choice == "exit") or (result == "Exit")):
        GameRun = False
        print("Game Exiting...")
    else:
        print(f"Computer chose: {computer_choice}")
        print(result)