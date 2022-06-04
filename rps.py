# Rock wins against scissors, 
# paper wins against rock, and 
# scissors wins against paper.
# Game becomes a tie when Player and CPU choices are the same.
# If game is a tie, the loop continues - Player can choose to play again or not.
# If either Player or CPU wins, loop stops and game ends. 

from random import choice

rps = ["R", "P", "S"]

# provide "how to play" guidelines to novices.
print("\n Hey! Let's play Rock, Paper, Scissors")
print("======================================")

print("Can you play this game? Or do you need heads up?\n")

try:
    answer = int(input("Enter 1 if you can play. Enter 2 if you want guidelines: "))
    if answer == 1:
        response = True
        print("\n")
    else:
        response = False
        print("\n When the game starts, you'll have to choose 'R', 'P', or 'S' \n \
            If you enter the same letter the computer randomly selects, then it's a tie.\
            But the folowing determines who wins based on what you entered and what the computer chooses:\n\
            1. R is greater than S | 2. P is greater than R | 3. S is greater than P.")

        print("\nYou may re-run the program now to start the game.")

except:
    print("Invalid answer: Enter 1 or 2. Try again")


## GAME
while response is True:

    # CPU randomly selects only after a player has entered a valid letter
    player_input = "incorrect"
    while player_input=="incorrect":

        player_choice = str(input("Choose R, P, or S: ")).upper()
        if player_choice not in rps:
            player_input = "incorrect"
            print("Invalid input.")

        elif player_choice in rps:
            player_input = "correct"
            cpu = choice(rps)

    
    print(f"Player ({player_choice}) : CPU ({cpu})")
    
    # check if it is a tie and ask user if they'd like to play again
    if player_choice == cpu:
        print("It's a tie")

        play_again = str(input("Play again? Yes/No: ")).upper()

        if play_again == "YES" or play_again == "Y":
            print("Yay! Let's continue \n")
            # continues if the user wants to
            response=True
            continue

        else: # breaks if the user doesn't type "yes" or "y"
            print("Ending game...")
            response=False
            break

    # if it's not a tie, these conditions check who won - Player or CPU    
    if player_choice=="R" and cpu=="S":
        print("You won :|")

    if player_choice=="P" and cpu=="R":
        print("You won :|")

    if player_choice == "S" and cpu == "P":
        print("You won :|")

    if cpu == "R" and player_choice == "S":
        print("CPU won :)")

    if cpu == "P" and player_choice == "R":
        print("CPU won :)")

    if cpu == "S" and player_choice == "P":
        print("CPU won :)")
    
    # breaks the loop
    else:
        break