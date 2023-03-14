# import modules
import csv
from statistics import mean

# create the path for the csv file
csv_path = ("/Users/jamesread/Downloads/Instructions 5/PyBank/Resources/budget_data.csv")

# set all variables to zero to start
months = 0
totalprofitloss = 0
previousrow = 0
currentchange = 0
sumofchanges = 0
averagechange = 0
greatestincrease = 0
greatestdecrease = 0

# set all variables to zero to start
months = 0
totalprofitloss = 0
previousrow = 0
currentchange = 0
sumofchanges = 0
averagechange = 0
greatestincrease = 0
greatestdecrease = 0

# create a list of the differences between the profit/loss from each month to the next
listofchanges = []

# open the csv file
with open (csv_path) as budget:
    # ignore the header row
    next(budget)
    # for each of the rest of the rows perform the following actions
    for row in csv.reader(budget):
        # add one to the total number of months
        months += 1
        # add the profit/loss value to the total amount of profits/losses
        totalprofitloss += int(row[1])
        
        # the current change is the difference between current profit/loss and previous profit/loss
        currentchange = int(row[1]) - previousrow
        # if current change is larger than the greatest increase so far, it will replace greatest increase
        if currentchange > greatestincrease:
            greatestincrease = currentchange
            # we will also store the month value for later
            greatestincreasemonth = row[0]
        # if current change is smaller than the greatest decrease so far, it will replace the greatest decrease
        elif currentchange < greatestdecrease:
            greatestdecrease = currentchange
            # also store the month value for later
            greatestdecreasemonth = row[0]
        # add the current change to our list of all of the changes over time
        listofchanges = listofchanges + [currentchange]
        # reset the previous row as the current row so we can use it on the next loop
        previousrow = int(row[1])

# remove the first value from list of changes, because we do not want to include the difference between the first value and 0
listofchanges.pop(0)

# find the average of all of the values in our list of changes
averagechange = mean(listofchanges)

# print our results
print("Financial Analysis")
print("--------------------")
print("Total Months: " + str(months))
print("Total: $" + str(totalprofitloss))
print("Average Change: $" + str(averagechange))
print("Greatest Increase in Profits: " + greatestincreasemonth + " ($" + str(greatestincrease) + ")")
print("Greatest Decrease in Profits: " + greatestdecreasemonth + " ($" + str(greatestdecrease) + ")")
