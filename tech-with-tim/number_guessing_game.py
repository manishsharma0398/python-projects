import random

print("\nHello, Welcome to Number Guesser, Let's test your number guesssing ability.\n")

rounds = int(input("How many rounds you want to play ? "))

score = 0


def get_score():
    print(f"\nYour score is {score} out of {rounds}")
    print("-----------------------------------")


get_score()

for round in range(1, rounds + 1):
    choice = int(input("Enter number (between 1 to 10): "))
    answer = random.randrange(1, 10)
    if choice == answer:
        score += 1
        print("You chose correct number")
    else:
        print(f"Oops, it is not a correct number. Correct number was {answer}")
    get_score()
