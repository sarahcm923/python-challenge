# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# define variables
vote_counter = 0
khan_count = 0
Khan = 0
correy_count = 0
Correy = 0
li_count = 0
Li = 0
otooley_count = 0
OTooley = 0
cand_list = []
winner = 0

csvpath = os.path.join('Resources/', 'election_data.csv')

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # loop through rows
    for row in csvreader:
        vote_counter += 1

        if (row[2] == "Khan"):
            khan_count +=1
        elif (row[2] == "Correy"):
            correy_count +=1
        elif (row[2] == "Li"):
            li_count +=1
        elif (row[2] == "O'Tooley"):
            otooley_count +=1

Khan = round((khan_count / vote_counter)* 100,4) 
Correy = round((correy_count / vote_counter)* 100,4) 
Li = round((li_count / vote_counter) * 100,4)
OTooley = round((otooley_count / vote_counter)* 100,4) 

cand_list = [Khan , Correy , Li , OTooley]
winner = cand_list.index(max(cand_list))
cand_name = ["Khan","Correy","Li","O'Tooley"]
winner_name = cand_name[winner]

print("***")
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(vote_counter))
print("----------------------------")
print(cand_name[0] + ": " + str(cand_list[0]) + "% (" + str(khan_count) + ")")
print(cand_name[1] + ": " + str(cand_list[1]) + "% (" + str(correy_count) + ")")
print(cand_name[2] + ": " + str(cand_list[2]) + "% (" + str(li_count) + ")")
print(cand_name[3] + ": " + str(cand_list[3]) + "% (" + str(otooley_count) + ")")
print("----------------------------")
print("Winner: " + winner_name)
print("----------------------------")
print("***")

#export to file
# Specify the file to write to
output_path = os.path.join('python-challenge/PyPoll', "election_results_output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as file:

    file.writelines("***\n")
    file.writelines("Election Results\n")
    file.writelines("----------------------------\n")
    file.writelines("Total Votes: " + str(vote_counter) + "\n")
    file.writelines("----------------------------\n")
    file.writelines(cand_name[0] + ": " + str(cand_list[0]) + "% (" + str(khan_count) + ")\n")
    file.writelines(cand_name[1] + ": " + str(cand_list[1]) + "% (" + str(correy_count) + ")\n")
    file.writelines(cand_name[2] + ": " + str(cand_list[2]) + "% (" + str(li_count) + ")\n")
    file.writelines(cand_name[3] + ": " + str(cand_list[3]) + "% (" + str(otooley_count) + ")\n")
    file.writelines("----------------------------\n")
    file.writelines("Winner: " + winner_name + "\n")
    file.writelines("----------------------------\n")
    file.writelines("***\n")    