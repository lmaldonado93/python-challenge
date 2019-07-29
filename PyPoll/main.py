import os
import csv
from collections import Counter


csvpath=os.path.join("Resources", "election_data.csv")

total_votes = []
candidates = []
percentage = []
votes_count = Counter()

with open(csvpath, newline='') as csvfile:
    poll = csv.reader(csvfile,delimiter=',')
    header = next(poll)
    for row in poll:

        total_votes.append(row[0])
        candidates.append(row[2])
        
    sum_total_votes = len(total_votes)
    list_of_candidates = set(candidates)

    for name in candidates:

        votes_count[name] += 1
    
    
    names = tuple(votes_count.keys())
    votes = tuple(votes_count.values())
    winner = max(zip(votes_count.values(), votes_count.keys()))

    for x in votes:
        percentage.append((int(x)/sum_total_votes)*100)


print ("Election Results")
print ("------------------------" )
print(f"Total Votes:  {sum_total_votes}")
print ("------------------------" )
for x in range(len(names)):
      print (f"{names[x]} :  {str(round(percentage[x],1))}%  ({str(votes[x])})")
print ("------------------------")
print (f"Winner:  {winner[1]}" )
print ("------------------------")

output_file = os.path.join("Polls_Analysis.txt")

with open(output_file, "w", newline="") as file:
    writer = open(output_file, 'w')

writer.write("Election Results\n")
writer.write("------------------------\n" )
writer.write(f"Total Votes:  {sum_total_votes}\n")
writer.write("------------------------\n" )
for x in range(len(names)):
      writer.write(f"{names[x]} :  {str(round(percentage[x],1))}%  ({str(votes[x])})\n")
writer.write("------------------------\n")
writer.write(f"Winner:  {winner[1]}\n" )
writer.write("------------------------\n")
