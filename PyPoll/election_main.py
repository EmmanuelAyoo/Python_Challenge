import os

import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

# Set variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

khan_percent = 0.000
correy_percent = 0.000
li_percent = 0.000
otooley_percent = 0.000

# Open csv file
with open(csvpath) as csvfile:

     #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
 
    # Read the header row first
    csv_header = next(csvreader)

     # Each row is read as a row
    for row in csvreader:

        #calcluate the Total number of votes cast
        total_votes = total_votes + 1

    #calculate total number of votes for each candidate
        if (row[2] == 'Khan'):
            khan_votes = khan_votes + 1
    
        elif (row[2] == 'Correy'):
            correy_votes = correy_votes + 1

        elif (row[2] == 'Li'):
            li_votes = li_votes + 1 

        else: 
            otooley_votes = otooley_votes + 1

    #calculate percentage of votes per candidate
    khan_percent = round(khan_votes / total_votes*100, 3)

    correy_percent = round(correy_votes / total_votes*100, 3)
    
    li_percent = round(li_votes / total_votes*100, 3)

    otooley_percent = round(otooley_votes / total_votes*100, 3)

    
    #Calculate winner based on popular vote
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes) 

    if winner == khan_votes:
        winner_name = 'Khan'

    elif winner == correy_votes:
        winner_name = 'Correy'    

    elif winner == li_votes:
        winner_name = 'Li'

    else:
        winner_name = 'Otooley'

    #Print Results
    print(f"ELECTION RESULTS")
    print("================================")
    print(f"TOTAL VOTES: {total_votes}")
    print("--------------------------------")
    print(f"Khan: {khan_percent}00% ({khan_votes})")
    print(f"Correy: {correy_percent}00% ({correy_votes})")
    print(f"Li: {li_percent}00% ({li_votes})")
    print(f"Otooley: {otooley_percent}00% ({otooley_votes})")
    print("---------------------------------")
    print(f"WINNER: {winner_name}")
    print("===============================")

#Export script to a text file
output_file = os.path.join('..', 'PyPoll', 'Resources', 'election_data.text')

# Open file with write mode
with open(output_file, 'w') as txtfile:

# Write out script in text file
    txtfile.write(f"ELECTION RESULTS\n")
    txtfile.write(f"====================\n")
    txtfile.write(f"TOTAL VOTES: {total_votes}\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Khan: {khan_percent}00% ({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent}00% ({correy_votes})\n")
    txtfile.write(f"Li: {li_percent}00% ({li_votes})\n")
    txtfile.write(f"Otooley: {otooley_percent}00% ({otooley_votes})\n")
    txtfile.write(f"-----------------------------\n")
    txtfile.write(f"WINNER: {winner_name}\n")
    txtfile.write(f"=========================\n")
    






















    