"""Print out a range of numbers starting from the last printed one."""
user_play = "y"
saved_number = 0

while user_play == "y":
    user_number = int(input("Please enter a number > 0! "))
    for i in range(1, user_number + 1):
        print(f"{i + saved_number}")
    saved_number = saved_number + user_number
    user_play = input("Continue: (y)es or (n)o? ")
