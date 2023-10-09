
from pathlib import Path
import csv
from datetime import datetime

csvpath=Path("/Users/pigeoneyevideography/Desktop/module2/Starter_Code_2/PyBank/Resources/budget_data.csv")

total_months = 0
month_of_chnage = []
net_change_list = []
greatest_increase = ['',0]
greatest_decrease = ['',9999999]
total_net = 0

with open(csvpath, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    first_row = next(reader)
    total_months = total_months+1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])
    for row in reader:
        total_months = total_months+1
        total_net = total_net+int(row[1])
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_chnage = month_of_chnage + [row[0]]
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
net_monthly_avg = round(sum(net_change_list) / len(net_change_list),3)


with open('financial_analysis.txt','w') as fa:
    fa.write(f'Financial Analysis\n')
    fa.write(f'------------------------\n')
    fa.write(f'Total months: {total_months}\n')
    fa.write(f'Toal: ${total_net}\n')
    fa.write(f'Average Chnage: ${net_monthly_avg}\n')
    fa.write(f'Greatest Increase in Profits: {greatest_increase[0]} ${greatest_increase[1]}\n')
    fa.write(f'Greatest Decrease in profits: {greatest_decrease[0]} ${greatest_decrease[1]}\n')
    