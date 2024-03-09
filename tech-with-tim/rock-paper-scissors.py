import random

print("\nRock, Papers and Scissors\n")

name = input("Please enter your name: ")

options = ["rock", "paper", "scissor"]

user_winning_rules = {
    "rock": {"computer": "scissor"},
    "paper": {"computer": "rock"},
    "scissor": {"computer": "paper"},
}


ingame_choice_message = f"""
Please enter a number to select respective option:
Rock - 1
Paper - 2
Scissors - 3

Select an option (1, 2, or 3): """

user_choice = 0

initial_choice_message = f"\nHey {name}, {ingame_choice_message}"

user_choice = int(input(initial_choice_message))


def restart_game():
    global user_choice
    user_choice = int(input(ingame_choice_message))
    start_game()


def start_game():
    global user_choice
    if user_choice < 1 or user_choice > 3:
        print("Please enter a valid value!")
        restart_game()
    else:
        computer_choice = options[random.randint(0, len(options) - 1)]
        user_choice = options[user_choice - 1]

        print(
            f"""
            user choice: {user_choice}
        computer choice: {computer_choice}
"""
        )

        if computer_choice == user_choice:
            print("Its a draw!")
        elif user_winning_rules[user_choice]["computer"] == computer_choice:
            print("You Win!")
        else:
            print("Computer Wins!")

        print("\n----------------------------------\n")

        final_input = input("Press r to play again, any other key to exit: ")
        if final_input == "r":
            restart_game()
        else:
            print(f"\nGame Over! Thankyou {name} for playing")
            quit()


start_game()

# print(computer_choice)
