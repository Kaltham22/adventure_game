import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field"
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here,"
                " and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.")
    print_pause("\n")


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        if response in options:
            return response
        print_pause(f'Sorry, the option "{options}" is invalid. Try again!')


def field():
    player_won = ["Congratulations", "Good job", "Excellent"]
    player1 = random.choice(player_won)
    print_pause("You won!")
    print_pause(player1)
    get_play()


def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger"
                " and take the sword with you.")
    print_pause("You walk back out to the field.")
    print_pause("\n")
    field()


def play_again():
    play_again = valid_input("GAME OVER\n\n"
                             "Would you like to play again? "
                             "(y/n) ", ['y', 'n']).lower()
    if play_again == 'y':
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif play_again == 'n':
        print_pause("Thanks for playing! See you next time.")


def fight():
    print_pause("You do your best...")
    print_pause("but your dagger is no match for the troll.")
    print_pause("You have been defeated!")


def house():
    player_lost = ["The was not the greatest idea", "Hard luck"]
    player2 = random.choice(player_lost)
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when "
                "the door opens and out steps a troll.")
    print_pause("Eep! This is the troll's house!")
    print_pause("The troll attacks you!")
    print_pause("You feel a bit under-prepared for this,"
                " what with only having a tiny dagger.")

    choice = valid_input("Would you like to (1) fight or "
                         "(2) run away? ", ['1', '2']).lower()
    if choice == '1':
        fight()
        print_pause(player2)
        print_pause("You lost!")
        play_again()
    elif choice == '2':
        print_pause("You run back into the field. Luckily,"
                    " you don't seem to have been followed.")
        print_pause("Good choice, you made it away safely.")
        print_pause("\n")
        field()


def get_play():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    response = valid_input("What would you like to do?\n"
                           "Please enter 1 or 2.\n", ['1', '2']).lower()
    if response == '1':
        house()
    elif response == '2':
        cave()


def play_game():
    intro()
    get_play()


play_game()
