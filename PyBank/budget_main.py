# Import os
import os

# Import csv module
import csv

# Start out all totals as zero values 
total_months = 0

net_revenue = 0

monthly_change = []

month_count = []

greatest_increase = 0

greatest_increase_date = 0

greatest_decrease = 0

greatest_decrease_date = 0

# Creat file path across operating system 
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# Open csv file
with open(csvpath) as csvfile:

    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
 
    # Read the header row first
    csv_header = next(csvreader)

    # Each row is read as a row
    for row in csvreader:

        # Calculate the total number of months 
        total_months = total_months + 1    

        # Calculate monthly net revenue
        net_revenue = net_revenue + int(row[1])

        # Calculate net change per month
        previous_row = int(row[1])
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        month_count.append(row[0])
        
    # Calculate the Greatest Increase in profits
    if int(row[1]) > greatest_increase:
        greatest_increase = int(row[1])
        greatest_increase_date = row[0]

    # Calculate the Greatest Decrease in profits   
    if int(row[1]) < greatest_decrease:
        greatest_decrease = int(row[1])
        greatest_decrease_date = row[0] 

    # Calculate the Average and Date
    average_change = sum(monthly_change) / total_months    

    #calculate the highest and lowest month    
    highest_month = max(monthly_change)
    lowest_month = min(monthly_change)
 
    # Print Analysis
    print(f"FINACIAL ANALYSIS")
    print("======================")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_revenue}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_date}, (${highest_month})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date}, (${lowest_month})")
    print("======================")

# Export script to a text file
output_file = os.path.join('..', 'PyBank', 'Resources', 'budget_data.text')

# Open file with write mode
with open(output_file, 'w') as txtfile:

# Write out script in text file
    txtfile.write(f"FINANCIAL ANALYSIS\n")
    txtfile.write(f"====================\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_revenue}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date}, (${highest_month})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date}, (${lowest_month})\n")
    txtfile.write(f"====================\n")
