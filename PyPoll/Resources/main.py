import os
import csv

# Set File Path for Input and Output
csvpath = os.path.join('PyPoll/Resources/election_data.csv')
file_to_output = "election_results.txt"

# Declaring the Variables 
total_votes = 0
candidates = []
candidate_votes = {}
winner_count = 0
winner = ''

with open('election_data.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
 
    for row in csvreader:

        total_votes += 1

        candidate = row["Candidate"]

        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1
        
        candidate_votes[candidate] = candidate_votes[candidate] + 1

with open(file_to_output, 'w') as txt_file:
    election_header = (
        f"Election Results\n"
        f"---------------\n")
    s1_lines = (
        f"---------------\n")
    txt_file.write(election_header)

    
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(total_votes)*100
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        txt_file.write(voter_output)
    txt_file.write(s1_lines)   

   
        
    winning_summary = (
        f"Winner: {winner}"
    )
    print(winning_summary)
    txt_file.write(winning_summary)