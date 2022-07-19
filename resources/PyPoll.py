"""
In this project, our final Python script will need to 
be able to deliver the following information when the 
script is run: 

    1. Total number of votes cast
    2. A complete list of candidates who received votes
    3. Total number of votes each candidate received
    4. Percentage of votes each candidate won
    5. The winner of the election based on popular vote

Algorithm
    1. Open file with csv reader.
    2. Iterate over rows.
    3. Store values in a dictionary.
        3.1. Create a dictionary per Candidate if it has none.
        3.2. Create a new list per County if it has none.
    4. Remove the header row from the dictionary.
    5. Get the list of candidates from dictionary keys.
    6. Iterate over Candidates and Counties to get the votes total.
"""
import csv
from pathlib import Path


# Inputs.
path = Path.cwd() / Path("resources")
file_name = "election_results.csv"
election_results = {}
# Outputs.
total_votes = 0
candidate_list = []
candidate_votes = {}
vote_percentage = {}
election_winner = ""

# Read dataset.
with open(path / file_name, "r") as file:
    file = csv.reader(file, delimiter = ",")
    for row in file:
        candidate = row[2]
        county = row[1]
        ballot_id = row[0]
        if candidate not in election_results.keys():
            election_results[candidate] = {}
        if county not in election_results[candidate].keys():
            election_results[candidate][county] = []
        election_results[candidate][county].append(ballot_id)

# Process dataset.
election_results.pop("Candidate")
candidate_list = list(election_results.keys())
for candidate in election_results:
    candidate_votes[candidate] = 0
    for county in election_results[candidate]:
        number_of_votes = len(election_results[candidate][county])
        candidate_votes[candidate] += number_of_votes
        total_votes += number_of_votes

# Obtain percentages and winner.
for candidate in candidate_votes:
    vote_percentage[candidate] = candidate_votes[candidate] / total_votes
election_winner = list(vote_percentage.keys())[0]
for candidate in vote_percentage:
    if vote_percentage[candidate] > vote_percentage[election_winner]:
        election_winner = candidate

print("--------------------")
print("Election Results.")
print("--------------------")
print("Here are this year's candidates:")
for i, candidate in enumerate(candidate_list):
    print(f"{i + 1}. {candidate}")
print(f"They gathered a total of \033[1m{total_votes}\033[0m combined votes.")
for candidate in candidate_votes:
    print(
        f"-> {candidate} gathered {candidate_votes[candidate]} votes "
        f"with \033[1m{vote_percentage[candidate]* 100:.2f}%\033[0m."
    )
print(f"And the winner of the election is \033[1m{election_winner}\033[0m!")