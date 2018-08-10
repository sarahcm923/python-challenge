# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('/Users/sarahsteimle/CWCL201807DATA2-Class-Repository-DATA/Week3Python/Day2/Activities/08-Stu_ReadNetFlix/Resources', 'netflix_ratings.csv')

found = False

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

# define variables
month_counter = 0
profit_increase = 0
profit_decrease = 0
net_profit_loss = 0
average_change = 0.00

# loop through rows
i = 1

for row[1] in csvreader:
    month_counter = month_counter + 1

    if (double(column[i]) - double(column[i-1]) > profit_increase):
        profit_increase = double(column[i]) - double(column[i-1])   
    elif (profit_decrease > double(column[i]) - double(column[i-1])):
        profit_decrease = double(column[i]) - double(column[i-1])

    net_profit_loss = net_profit_loss + double(column[i])

    i +=1


average_change = (net_profit_loss / month_counter)

print (blah blah)
#export to file