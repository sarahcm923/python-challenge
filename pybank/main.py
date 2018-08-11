# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# define variables
average_change = 0
month_counter = 0
last_row = 0
profit_increase = 0
profit_inc_month = ""
profit_decrease = 0
profit_dec_month = ""
net_profit_loss = 0

csvpath = os.path.join('/Users/sarahsteimle/CWCL201807DATA2-Class-Repository-DATA/Homework/hmw3Python/PyBank/Resources', 'budget_data.csv')

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # loop through rows
    for row in csvreader:
        month_counter = month_counter + 1
        current_row = int(row[1])

        if ((current_row - last_row) > profit_increase):
            profit_increase = current_row - last_row
            profit_inc_month = row[0]

        elif (profit_decrease > (current_row - last_row)):
            profit_decrease = current_row - last_row
            profit_dec_month = row[0]

        last_row = current_row
        net_profit_loss = net_profit_loss + current_row
        

average_change = ( net_profit_loss / month_counter)
average_change = round(average_change,2)

print("")
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(month_counter))
print("Total: $" + str(net_profit_loss))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(profit_inc_month) + " ($" + str(profit_increase) + ")")
print("Greatest Decrease in Profits: " + str(profit_dec_month) + " ($" + str(profit_decrease) + ")")
print("'''")

#export to file
# Specify the file to write to
output_path = os.path.join('/Users/sarahsteimle/CWCL201807DATA2-Class-Repository-DATA/Homework/hmw3Python/python-challenge/PyBank', "budget_data_output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as file:

    #for line in file:
        # Write the first row (column headers)
        file.writelines("'''\n")
        file.writelines("Financial Analysis\n")
        file.writelines("----------------------------\n")
        file.writelines("Total Months: " + str(month_counter)+ "\n")
        file.writelines("Total: $" + str(net_profit_loss)+ "\n")
        file.writelines("Average Change: $" + str(average_change)+ "\n")
        file.writelines("Total Months: " + str(month_counter)+ "\n")
        file.writelines("Greatest Increase in Profits: " + str(profit_inc_month) + " ($" + str(profit_increase) + ")\n")
        file.writelines("Greatest Decrease in Profits: " + str(profit_dec_month) + " ($" + str(profit_decrease) + ")\n")
        file.writelines("'''\n")