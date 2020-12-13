import os
import csv

csvpath = os.path.join('./Resources/election_data.csv')

candidates = []
num_vote = 0
vote_count = []

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:

        #The total number of votes cast
        num_vote = num_vote + 1

        #A complete list of candidates who received votes
        candidate = row[2]

        
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_count[candidate_index] = vote_count[candidate_index] + 1
      
        else:
            candidates.append(candidate)
            vote_count.append(1)

percent = []
max_votes = vote_count[0]
max_index = 0

#The percentage of votes each candidate won
for count in range(len(candidates)):
    vote_percent = round(((vote_count[count]/num_vote)*100),1)
    percent.append(vote_percent)
    if vote_count[count] > max_votes:
        max_votes = vote_count[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]


print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_vote}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percent[count]}% ({vote_count[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

output_file = os.path.join("Analysis","analysis.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write("Election Results\n")
    datafile.write("--------------------------\n")
    datafile.write(f"Total Votes: {num_vote}\n")
    for count in range(len(candidates)):
        datafile.write(f"{candidates[count]}: {percent[count]}% ({vote_count[count]})\n")
    datafile.write("---------------------------\n")
    datafile.write(f"Winner: {winner}\n")
    datafile.write("---------------------------\n")