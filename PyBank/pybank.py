import os
csvpath = os.path.join('Resources', 'budget_data_1.csv')

import csv

months = []
revenue = []

with open(csvpath, newline='') as csvfile:
    csvfile.readline()
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)
    #  Each row is read as a row
    for row in csvreader:
        print(row)

        #Add months
        months.append(row[0])

        # Add revenue
        revenue.append(int(row[1]))

    #print(months)
    #print(revenue)

    #Determine the number of months included in dataset  
    month_count = len(months)
    print(month_count) 
   

    # Determine total amount gained over entire period
    total_revenue = sum(revenue)
    print(total_revenue)

    #Average change in revenue between months over entire period
    change_revenue = revenue[-1] - revenue[0] 
    average_change = change_revenue/month_count

# make document into a dictionary, sum up value pairs 
#rev_dict = dict(zip(months, revenue))


#Greatest increase in Revenue with a date and amount in entire period
max_rev = max(revenue)
a = 0
for x in revenue:
    if x == max_rev: 
        print(months[a], revenue[a])
    a = a + 1

#Greatest Decrease in revenue with a date and amount in entire period
min_rev = min(revenue)
a = 0
for x in revenue:
    if x == min_rev: 
        print(months[a], revenue[a])
    a = a + 1
#import it to a text file

file = open("pybank.txt", "w")
file.write("Financial Analysis\n")
file.write("---------------------------\n")
file.write("Total Months:%s\n" % month_count)
file.write("Total Revenue:%s\n" % (total_revenue))
file.write("Average Revenue Change:%s\n" % (average_change))
file.write("Greatest Increase in Revenue:%s\n" % (max_rev))
file.write("Greatest Decrease in Revenue:%s\n" % (min_rev))
file.write("--------------------------- ")
file.close() 