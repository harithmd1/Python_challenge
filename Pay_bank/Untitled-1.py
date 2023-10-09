    
from pathlib import Path
import csv

csvpath = Path("/Users/pigeoneyevideography/Desktop/module2/Starter_Code_2/PyBank/Resources/budget_data.csv")

Data = {}

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(csv_header)

Total_Months=0
Profits_and_Losses=0
Total=0
Average=0
Greatest_Increase=0
Greatest_Decreae=0

for row in csvreader:
        Date = row[0]
        Profits_and_Losses = int(row[1])
        Data[Date]=Profits_and_Losses
Print(Data)

for Profits_and_losses in csvreader:
     Total += Profits_and_losses
     Total_Months +=1
     Average=Total/Total_Months

if Greatest_Decrease == 0:
    Greatest_Decrease = Profits_and_Losses
elif Profits_and_Losses > Greatest_Increase:
    max_salary = Profits_and_Losses
elif Profits_and_Losses < Greatest_Decrease:
    Greatest_Decrease = Profits_and_Losses

print("Financial Analysis")
Print("------------------")
Print(f"Total Months: {Total_months}")
Print("Total: ${Total}") 
print("Average Change: ${Average}") 
Print("Greatest Increase in Profits: $({Greatest_Increase})")
print("Greatest Decrease in Profits: $({Greatest_Decrease})")

