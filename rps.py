import random

game_count=1
win=0

while True:
    choices = ["rock","paper","scissors"]

    print("Game No.",game_count)
    print("Rounds won",win)
    
    computer = random.choice(choices)
    player= None
    
    while player not in choices:                               

        player= input("Rock,Paper or Scissors?").lower()

        if computer == player:
            print("Computer:", computer)
            print("Player:", player)
            print("It's a tie!")

        elif computer == "rock":
            if player == "paper":
                print("Computer:", computer)
                print("Player:", player)
                print("You Win!")
                win += 1
            else:
                print("You Lose")
     
        elif computer == "paper":
            if player == "scissors":
                print("Computer:", computer)
                print("Player:", player)
                print("You Win!")
                win += 1
            else:
                print("You Lose")                  

        elif computer == "scissors":
            if player == "rock":
                print("Computer:", computer)
                print("Player:", player)
                print("You Win!")
                win +=1
            else:
                print("You Lose")

        else:
            print("Choose between the options given, please.")        

    game_count += 1


    opti=input("Do you want to play again?(Yes/No)").lower()
    if opti != "yes":
        break
print("Bye!") 