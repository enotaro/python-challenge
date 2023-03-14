# import csv module
import csv

# create path to csv
csv_path = ("/Users/jamesread/Downloads/Instructions 5/PyPoll/Resources/election_data.csv")

# set total number of votes to zero
totalvotes = 0

# open the csv
with open (csv_path) as votes:
    # skip the header row
    next(votes)
    # for each row perform the following actions
    for row in csv.reader(votes):
        # add 1 to the total number of votes
        totalvotes += 1

# import counter to allow us to count the number of occurences of each candidate's name
from collections import Counter

# open the csv
with open(csv_path, 'r') as election:
    # create a dictionary that will count the number of votes for each candidate
    votesdict = Counter(row[2] for row in csv.reader(election))   

# store the number of votes for each candidate
stockhamvotes = votesdict['Charles Casper Stockham']
degettevotes = votesdict['Diana DeGette']
doanevotes = votesdict['Raymon Anthony Doane']

# convert the number of votes for each candidate to a percentage
stockhampercent = (stockhamvotes/totalvotes)*100
degettepercent = (degettevotes/totalvotes)*100
doanepercent = (doanevotes/totalvotes)*100

# print your results
print("Election Results")
print("----------------------")
print("Total Votes: " + str(totalvotes))
print("----------------------")
print("Charles Casper Stockham: "+ str(stockhampercent) + "% (" + str(stockhamvotes) + ")")
print("Diana DeGette: " + str(degettepercent) + "% (" + str(degettevotes) + ")")
print("Raymon Anthony Doane: " + str(doanepercent) + "% (" + str(doanevotes) + ")")
print("----------------------")

# determine the winner based on which vote count is the largest
# if Stockham had more votes than both DeGette and Doane, then he wins
if stockhamvotes > degettevotes and stockhamvotes > doanevotes:
    print("Winner: Charles Casper Stockham")
# if DeGette had more votes than both Stockham and Doane, then she wins
elif degettevotes > stockhamvotes and degettevotes > doanevotes:
    print("Winner: Diana DeGette")
# otherwise, Doane wins
else:
    print("Winner: Raymon Anthony Doane")

    
# create text file
txt = open('election.txt', 'w')
txt.write('Election Results ---------------------- Total Votes: 369711 ---------------------- Charles Casper Stockham: 23.04854332167558% (85213) Diana DeGette: 73.81224794501652% (272892) Raymon Anthony Doane: 3.1392087333079077% (11606)---------------------- Winner: Diana DeGette')
txt.close()
