"""Find video name in CSV file and write (append) to a file with the results."""
import os
import csv


video = input("What show or movie are you looking for? ")
csvpath = os.path.join("Resources", "netflix_ratings.csv")
outputpath = os.path.join("output", "video_result.txt")
found = False

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if row[0] == video:
            found = True
            with open(outputpath, "a") as textfile:
                # title, rating level, movie rating ()
                contents = f"Title: {row[0]}, Rating Level: {row[1]} ({row[2]})"
                textfile.write(contents)
                print(contents)
            break
    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")
