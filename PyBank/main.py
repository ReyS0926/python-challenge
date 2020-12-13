import os
import csv

csvpath = os.path.join('./Resources/budget_data.csv')

Month = []
Profit_Losses = []
Avg_Change = []


with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
  
    # The total number of months included in the dataset
        Month.append(row[0])
    
    #The net total amount of "Profit/Losses" over the entire period
        Profit_Losses.append(int(row[1]))
    
    #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    for r in range(len(Profit_Losses)-1):
        Avg_Change.append(Profit_Losses[r+1]-Profit_Losses[r])

    #The greatest increase in profits (date and amount) over the entire period
max_increase_value = max(Avg_Change)
max_decrease_value = min(Avg_Change)
max_increase_month = Avg_Change.index(max(Avg_Change)) + 1
max_decrease_month = Avg_Change.index(min(Avg_Change)) + 1 

print("Financial Analysis")
print("--------------------------------")
print(f"The total number of months included in the dataset is {(len(Month))}")
print(f"The net total amount of Profit/Losses over the entire period is ${(sum(Profit_Losses)):,.2f}")
print(f"Average Change: ${round(sum(Avg_Change)/len(Avg_Change),2):,.2f}")
print(f"Greatest Increase in Profits: {Month[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {Month[max_decrease_month]} (${(str(max_decrease_value))})")

output_file = os.path.join("Analysis","analysis.txt")

with open(output_file, "w", newline="") as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("--------------------------------\n")
    datafile.write(f"The total number of months included in the dataset is {(len(Month))}\n")
    datafile.write(f"The net total amount of Profit/Losses over the entire period is ${(sum(Profit_Losses)):,.2f}\n")
    datafile.write(f"Average Change: ${round(sum(Avg_Change)/len(Avg_Change),2):,.2f}\n")
    datafile.write(f"Greatest Increase in Profits: {Month[max_increase_month]} (${(str(max_increase_value))})\n")
    datafile.write(f"Greatest Decrease in Profits: {Month[max_decrease_month]} (${(str(max_decrease_value))})\n")