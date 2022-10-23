
import random

moves = ["rock", "paper", "scissors"]

game_instructions = "At the beginning of each duel, you will be asked to select between rock, paper or scissors." \
    " Our razzle dazzle randomizer will select the computer's weapon of choice at random and your duel shall commence." \
        " \n\nIf the borings of life are calling your name, you can exit the game at any time by entering, 'quit' and should" \
            " the luck of life be more like a dooms day cloud, after five losses, you will be given the option to select dynamite." \
                " \n\nMake your selection carefully because this dynamite is highly unstable and will blow up not just your opponets " \
                    "weapon, but the entire game. \n\nGood luck noble warrior, you're going to need it."

user_gamertag = input("What is your name/gamertag? ")

print(game_instructions)

def play():
    play_options = ["rock", "paper", "scissors"]
    play = True

    win = 0
    lose = 0
    tie = 0

    while play:
        if lose >= 5:
            dyn = input("Do you want to use dynamite?") 

            if dyn == "yes":
                    print("KABOOM!")
                    print(f"GAME OVER\n {user_gamertag}'s Game Results: \n win: {win} \n lose: {lose} \n tie {tie}")
                    break

        user_input = input("Enter (rock, paper, scissors, quit): ")
        computer_input =  (random.choice(play_options))
        print(computer_input)
                
        if user_input == "rock":
            if computer_input == "scissors":
                win += 1
                print("Rock destroyed scissors! You win!")
            elif computer_input == user_input:
                tie += 1
                print("You tied")
            else:
                lose += 1
                print("Paper smothered rock to death! You lose.")

        elif user_input == "paper":
            if computer_input == "rock":
                win += 1
                print("Paper smothered rock to death! You win!")
            elif computer_input == user_input:
                tie += 1
                print("You tied!")
            else:
                lose += 1
                print("Scissors chopped paper to pieces! You lose."  )

        elif user_input == "scissors":
            if computer_input == "paper":
                win += 1
                print("Scissors chopped paper to pieces! You win!")
            elif computer_input == user_input:
                tie += 1
                print("You tied!")
            else:
                lose += 1
                print("Rock destroyed scissors! You lose.")

        elif user_input == "quit":
            print(f"GAME OVER\n {user_gamertag}'s Game Results: \n win: {win} \n lose: {lose} \n tie {tie}")
            play = False

    return "\nToday's entertainment has been brought to you by Pegasus and Hercules!"

print(play())
