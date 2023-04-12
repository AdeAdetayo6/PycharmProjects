#def hello():
 #   print("Enjoy your day! ") #Function1

#def bye():
 #   print("Have a Good time! ") #Function2

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - (38/101)

print("")
print("Working with Games: Rock,Paper,Scissors! ")

import random

while True:
    list = ["rock","paper","scissors"]

    computer = random.choice(list)
    player = None

    while player not in list:
        player = input("rock, paper, or scissors?: ").lower()
        if player not in list:
            print("Please input valid selection. ")

    if player == computer: # here is the sequence if player and computer pick the same
        print("Computer: ",computer)
        print("Player: ",player)
        print("Draw!")
    elif player == "rock": # here is the sequence where player picks ROCK, conditioning for responses on what computer picks
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Lose!")
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Win!")

    elif player == "Scissors": # here is the sequence where player picks Scissors, conditioning for responses on what computer picks
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Lose!")
        if computer == "Paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Win!")

    elif player == "paper": # here is the sequence where player picks PAPER, conditioning for responses on what computer picks
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Win!")
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Lose!")

    replay = input("Replay Game?: (Yes/No)").lower()
    if replay != "yes":
        break
print("Duece! ")
