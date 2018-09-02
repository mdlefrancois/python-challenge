#write a Python script that will find:

#The total number of months included in the dataset
#The total net amount of "Profit/Losses" over the entire period
#The average change in "Profit/Losses" between months over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Import the necessary dependencies for os.path.join()
import os
import csv
import sys

# Lists to store data
date = []
prices = []

# Read in a .csv file
budget_csv = os.path.join("budget_data.csv")

with open('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #line counter
    line_count = 0

    #Initialize the total price variable
    Total_Price = 0

    #parse data input
    for row in csv_reader:
        if line_count == 0:
#            print(f'Column names are {", ".join(row)}')
            line_count += 1

        else:
#           print(f'\t{row[0]}  {row[1]} ')
            line_count += 1

            # Add date for each 
            date.append(row[0])

            # Add price for each list in the CSV file
            prices.append(int(row[1]))          
#print(f'Processed {line_count} lines.')

#Initialize variables and loop through information
#create greatest increase/decrease variables
Price_Change = 0.0
TrkPriceChange = 0.0
Grt_Prof_Inc = 0.0
Grt_Prof_Dec = 0.0
for i in range(len(prices)):
    
    #Sum the total budget
    Total_Price += prices[i]

    #calculate price change line by line
    if i >= 1:
        Price_Change += float(prices[i]) - float(prices[i-1])
        TrkPriceChange = float(prices[i]) - float(prices[i-1])
    
    #The greatest increase/decrease in profits/losses over the entire period
    if  TrkPriceChange > Grt_Prof_Inc:
        Grt_Prof_Inc = float(prices[i]) - float(prices[i-1])
        Grt_Prof_Inc_Month = date[i]
    elif TrkPriceChange <= Grt_Prof_Dec:
        Grt_Prof_Dec = float(prices[i]) - float(prices[i-1])
        Grt_Prof_Dec_Month = date[i]


#calculate the average change in price
AvgChange = round((Price_Change)/line_count, 2)

# Write to the screen
print('Financial Analysis')
print('--------------------------' )
print('Total Months: ' + str(line_count) )
print('Total: $' + str(Total_Price))
print('Average  Change: $' + str(AvgChange) )
print('Greatest Increase in Profits: ' + str(Grt_Prof_Inc_Month) + " $(" + str(Grt_Prof_Inc) + ')')
print('Greatest Decrease in Profits: ' + str(Grt_Prof_Dec_Month) + " $(" + str(Grt_Prof_Dec) + ')')
    
#  Open the output file
out_file = open("FinancialAnalysis.txt", "w")

# Write to the output file
out_file.write('Financial Analysis' + '\n')
out_file.write('--------------------------' + '\n')
out_file.write('Total Months: ' + str(line_count) +'\n')
out_file.write('Total: $' + str(Total_Price)     +'\n')
out_file.write('Average  Change: $' + str(AvgChange) +'\n')
out_file.write('Greatest Increase in Profits: ' + str(Grt_Prof_Inc_Month) + ' $(' + str(Grt_Prof_Inc) + ')' + '\n')
out_file.write('Greatest Decrease in Profits: ' + str(Grt_Prof_Dec_Month) + ' $(' + str(Grt_Prof_Dec) + ')')
