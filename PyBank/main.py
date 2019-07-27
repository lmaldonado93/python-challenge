import os
import csv

csvpath=os.path.join("Resources", "budget_data.csv")

total_months = []
net_total = []
Average_Change_Monthly = []

with open(csvpath, newline='') as csvfile:
    budget=csv.reader(csvfile, delimiter=',')
    header = next(budget)
    for row in budget:

        total_months.append(row[0])
        net_total.append(int(row[1]))
    sum_total_months = len(total_months)
    sum_net_total = sum(net_total)
    
    for i in range(len(net_total)-1):
        Average_Change_Monthly.append(net_total[i+1]-net_total[i])
    overall_avg_change_monthly = round(sum(Average_Change_Monthly)/len(Average_Change_Monthly),2)

greatest_value = max(Average_Change_Monthly)
least_value  = min(Average_Change_Monthly)

greatest_value_monthly = Average_Change_Monthly.index(max(Average_Change_Monthly))+1
least_value_monthly = Average_Change_Monthly.index(min(Average_Change_Monthly))+1  

print("Financial Analysis")
print("---------------------")
print(f"Total Months:  {sum_total_months}")
print(f"Total:  ${sum_net_total}")
print(f"Average Change:  ${overall_avg_change_monthly}")
print(f"Greatest Increase in Profits: {total_months[greatest_value_monthly]} (${(str(greatest_value))})")
print(f"Greatest Decrease in Profits: {total_months[least_value_monthly]} (${(str(least_value))})")  

output_file = os.path.join("Financial_Analysis.txt")

with open(output_file, "w", newline="") as file:
    writer = open(output_file, 'w')

    writer.write("Financial Analysis\n")
    
    writer.write("---------------------\n")
   
    writer.write(f"Total Months:  {sum_total_months}\n")
    
    writer.write(f"Total:  ${sum_net_total}\n")
   
    writer.write(f"Average Change:  ${overall_avg_change_monthly}\n")
    
    writer.write(f"Greatest Increase in Profits: {total_months[greatest_value_monthly]} (${(str(greatest_value))})\n")
    
    writer.write(f"Greatest Decrease in Profits: {total_months[least_value_monthly]} (${(str(least_value))})\n") 