import os
import csv

output_file = os.path.join('.','budget_data.csv',)
text_path = 'output.txt'

total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_average = 0


with open(output_file,'r',encoding='UTF-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    
    header = next(csv_reader)

    for row in csv_reader:
        Date = (row[0])
        Profit_Losses = float(row[1])
        #Total of months and revenue from each row
        total_months += 1
        total_revenue = total_revenue + Profit_Losses

        #Average change in revenue between months over the entire period
        revenue_change = Profit_Losses - previous_revenue

        previous_revenue = Profit_Losses

        revenue_change_list = revenue_change_list + [revenue_change]

        month_of_change = [month_of_change] + [Date]

        if revenue_change>greatest_increase[1]:
            greatest_increase[1]= revenue_change
            greatest_increase[0] = Date

        #The greatest decrease in revenue (date and amount) over the entire period
        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1]= revenue_change
            greatest_decrease[0] = Date
    revenue_average = sum(revenue_change_list)/len(revenue_change_list)

    with open(text_path, 'w') as new_file:
        new_file.write("Financial Analysis\n")
        new_file.write("---------------------\n")
        new_file.write("Total Months: %d\n" % total_months)
        new_file.write("Total Revenue: $%d\n" % total_revenue)
        new_file.write("Average Revenue Change $%d\n" % revenue_average)
        new_file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
        new_file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))
       
    
open(text_path)