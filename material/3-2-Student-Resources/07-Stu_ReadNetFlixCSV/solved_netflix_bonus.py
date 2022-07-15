"""Read a file and find user input in first row and print it along second row."""
import os
import csv


video = input("What show or movie are you looking for? ")
path = os.path.join("Resources", "netflix_ratings.csv")
found = False

with open(path) as csv_file:
    csv_data = csv.reader(csv_file)
    for row in csv_data:
        if row[0] == video and not found:
            found = True
            print(f"{row[0]} is rated {row[1]}")

if not found:
    print("Sorry, we don't seem to have the video you are looking for!")
