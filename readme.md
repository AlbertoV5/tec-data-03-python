[Repository](https://github.com/AlbertoV5/tec-data-03-python)


# PyPoll Election Audit

In this project, we were given the task to find the results of an election by counting the votes in a large dataset. We were also looking for the following data:

1.  Total number of votes.
2.  List of candidates who received votes.
3.  Number of votes per candidate and their percentage.
4.  List of counties that had vote turnouts.
5.  County with the largest amount of vote turnouts.

We designed an algorithm that would do the work for us by feeding it a csv file and storing the results in a text file.


## Resources

Python version: `Python 3.7.13` VS Code version: `1.69.2`.

Dataset: `election_results.csv`.


## Election Audit Results

We found out that the there were `369,711` votes registered, from which `82.8%` came from Denver, the rest came from Jefferson `(10.5%)` and Arapahoe `(6.7%)`.

The winner of the election was `Diana DeGetter` with `73.8%` of the vote. These are the rest of the results:

| Candidate               | Votes   | Percentage |
|----------------------- |------- |---------- |
| Raymond Anthony Doane   | 11,606  | 3.1%       |
| Charles Casper Stockham | 85,212  | 23.0%      |
| Diana DeGette           | 272,892 | 73.8%      |

The following data was stored to the `election_analysis.txt` file.

```shell
cat election_analysis.txt
```

    
    Election Results
    -------------------------
    Total Votes: 369,711
    -------------------------
    
    County Votes:
    Jefferson: 10.5% (38,855)
    Denver: 82.8% (306,055)
    Arapahoe: 6.7% (24,801)
    
    -------------------------
    Largest County Turnout: Denver
    -------------------------
    Charles Casper Stockham: 23.0% (85,213)
    Diana DeGette: 73.8% (272,892)
    Raymon Anthony Doane: 3.1% (11,606)
    -------------------------
    Winner: Diana DeGette
    Winning Vote Count: 272,892
    Winning Percentage: 73.8%
    -------------------------


## Summary of the Python Problem

The following is a partial description of how to solve the problem using Python.

Importing the libraries and loading the data.

```python
import csv
from pathlib import Path

resources = Path.cwd() / "resources"
file_to_load = resources / "election_results.csv"
file_to_save = Path.cwd() / "election_analysis.txt"
```

Initializing variables.

```python
candidate_list = []
county_list = []
candidate_votes = {}
county_votes = {}
```

The most important part of the code was that we were able to check if the candidate name existed already in the dictionary, and if it didn&rsquo;t we would add it to the list only once and move on into just incrementing the vote count.

This is a reduced example of the process.

```python
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    for row in reader:
        candidate_name = row[2]
        county_name = row[1]
        # Check for candidate
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        # Check for county
        if county_name not in county_list:
            county_list.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

print(candidate_votes)
print(county_votes)
```

```org
{'Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606}
{'Jefferson': 38855, 'Denver': 306055, 'Arapahoe': 24801}
```

Then after that storing the results was a simple process as we can do whatever we want with the data stored in the dictionaries.

For example, printing the total votes or percentage of values from any key. As well as making sure that the totals match.

```python
total_votes_candidate = sum(candidate_votes.values())
total_votes_county = sum(county_votes.values())
assert total_votes_candidate == total_votes_county
print(f"Total Votes: {total_votes_candidate}")
print("Percentage for Diana DeGette:")
print(f"{100 * candidate_votes['Diana DeGette'] / total_votes_candidate:.2f}%")
```

```org
Total Votes: 369711
Percentage for Diana DeGette:
73.81%
```


## Closing Thoughts

Python does a great job on removing a lot of obstacles in between us as the users and the computer, as it&rsquo;s really easy to generate working code starting from a solid pseudocode / algorithm. Even if it&rsquo;s not the fastest in processing the data, it&rsquo;s definitely the tool that can get the job done in the least amount of time once you learn it.
