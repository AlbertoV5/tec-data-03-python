"""
PyPoll

In this project, our final Python script will need to
be able to deliver the following information when the
script is run:
    1. Total number of votes cast
    2. A complete list of candidates who received votes
    3. Total number of votes each candidate received
    4. Percentage of votes each candidate won
    5. The winner of the election based on popular vote

Algorithm
    1. Open file with csv reader and iterate over rows.
    2. Store values in a dictionary.
        2.1. Create a dictionary value per Candidate key if it has none.
        2.2. Create a list value per County per Candidate if it has none.
        2.3. If they exist, append ballot id to County per Candidate.
    3. Get candidates names via the dict keys, minus the header row.
    4. Count the number of votes with the length of the Ballot id list.
    5. Obtain percentages per Candidate using the total votes.
    6. Find the winner Candidate using the percentages.
    7. Print results to console.
    8. Save results to text file.
"""
import csv
from pathlib import Path


# Variables for inputs.
path = Path.cwd() / "resources"
data_filename = "election_results.csv"
results_filename = "election_results.txt"
# Variables for outputs.
election_results = {}
total_votes = 0
candidate_list = []
candidate_votes = {}
vote_percentage = {}
election_winner = ""
# 1. Read dataset.
with open(path / data_filename, "r") as file:
    file = csv.reader(file, delimiter=",")
    for row in file:
        candidate = row[2]
        county = row[1]
        ballot_id = row[0]
        # 2. Add data to dictionary
        if candidate not in election_results.keys():
            election_results[candidate] = {}
        if county not in election_results[candidate].keys():
            election_results[candidate][county] = []
        election_results[candidate][county].append(ballot_id)
# 3. Get candidates names.
election_results.pop("Candidate")
candidate_list = list(election_results.keys())
# 4. Count votes.
for candidate in election_results:
    candidate_votes[candidate] = 0
    for county in election_results[candidate]:
        number_of_votes = len(election_results[candidate][county])
        candidate_votes[candidate] += number_of_votes
        total_votes += number_of_votes
# 5. Obtain percentages.
for candidate in candidate_votes:
    vote_percentage[candidate] = candidate_votes[candidate] / total_votes
# 6. Find the winner.
election_winner = list(vote_percentage.keys())[0]
for candidate in vote_percentage:
    if vote_percentage[candidate] > vote_percentage[election_winner]:
        election_winner = candidate
# 7. Print results.
print_candidates = ""
for i, candidate in enumerate(candidate_votes):
    print_candidates += (
        f"{i + 1}. {candidate}: {vote_percentage[candidate]* 100:.1f}%"
        f"({candidate_votes[candidate]:,}).\n"
    )
print("-------------------------------")
print("Election Results.")
print("-------------------------------")
print(f"Total Votes: \033[1m{total_votes:,}\033[0m.")
print(print_candidates[:-2])
print("-------------------------------")
print(f"The winner is \033[1m{election_winner}\033[0m.")
print("-------------------------------")
# 8. Save results to text file.
with open(path / results_filename, "w+") as file:
    file.write(
        f"Election Results\n"
        f"-------------------------------\n"
        f"Total Votes {total_votes:,}\n"
        f"-------------------------------\n"
        f"{print_candidates}"
        f"-------------------------------\n"
    )
