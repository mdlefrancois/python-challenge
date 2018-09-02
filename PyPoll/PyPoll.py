#write a Python script that will:

#In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
#(Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

#The dataset is composed of three columns: Voter ID, County, and Candidate. 
#Your task is to create a Python script that analyzes the votes and calculates each of the following:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os
import csv
import sys

# Lists to store data
VoteID = []
County = []
Candidate = {}  #use a dictionary to populate candidates

# Read in a .csv file
election_csv = os.path.join("Resources", "election_data.csv")

#get data file and populate the lists
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')

    #line counter
    line_count = 0

    #parse data input
    for row in csv_reader:

        if line_count == 0:
            line_count += 1

        else:
            line_count += 1

            # Vote ID generation for each line
            VoteID.append(row[0])

            # Add county for each line in file
            County.append(row[1])

            #check to see if the candidates exist in the dictonary, if so give them some votes
            if row[2] in Candidate:
                Candidate[row[2]] += 1
            #otherwise set the vote back to 1
            else:
                Candidate[row[2]] = 1

#output check on unique voter id's
#print("total lines: " + str(line_count))

# Write to the screen
print("")
print('Election Results')
print('--------------------------' )
print('Total Votes: ' + str(line_count) )
print('--------------------------' )
for key, value in Candidate.items(): # This loop prints voting results for each candidate
  print (key + ": " + "{0:.1f}%".format(value/line_count * 100) + 
         " (" + str(value) + ")")
print ("\n--------------------------\n")
print ("Winner: " + max(Candidate, key=Candidate.get) ) # determine the winner using 
print ("\n--------------------------") 

# Now output same results to the output file
out_file = open("ElectionResults.txt", "w")

out_file.write ("Election Results" '\n')
out_file.write ("--------------------------\n")
out_file.write("Total Votes: " + str(line_count) + '\n')
out_file.write ("--------------------------\n")

#using dictionary keys loop through and summarize the candidates
for key, value in Candidate.items():
    out_file.write(key + ": " + "{0:.1f}%".format(value/line_count * 100) +
        " (" + str(value) + ")\n")
out_file.write ("\n--------------------------\n")
#List the winning candidate based on the max of the dictionary {"candidate": key}
out_file.write("Winner: " + max(Candidate, key=Candidate.get) + '\n')
out_file.write ("\n--------------------------")
