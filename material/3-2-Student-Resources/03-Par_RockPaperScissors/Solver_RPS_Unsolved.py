import random


print("Let's Play Rock Paper Scissors!")
options = ["r", "p", "s"]
computer_choice = random.choice(options)
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if user_choice == "r":
    if computer_choice == "r":
        print("We Tie.")
    elif computer_choice == "p":
        print("You loose!")
    elif computer_choice == "s":
        print("You win!")
elif user_choice == "p":
    if computer_choice == "r":
        print("You win!")
    elif computer_choice == "p":
        print("We Tie.")
    elif computer_choice == "s":
        print("You loose!")
elif user_choice == "s":
    if computer_choice == "r":
        print("You loose!")
    elif computer_choice == "p":
        print("You win!")
    elif computer_choice == "s":
        print("We tie!")
else:
    print("Pick a valid choice!")


print(f"I chose {computer_choice}")