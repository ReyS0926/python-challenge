import os
import csv

csvpath = os.path.join('./Resources/budget_data.csv')

Date = []

with open(csvpath, newline='', encoding='utf-8') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
  
    # The total number of months included in the dataset
        Date.append(row)
    print(len(Date))
    
    
    #The net total amount of "Profit/Losses" over the entire period


    #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


    #The greatest increase in profits (date and amount) over the entire period


    #The greatest decrease in losses (date and amount) over the entire period