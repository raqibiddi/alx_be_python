monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
#print(monthly_savings)
print("Your monthly savings are", "$", monthly_savings)
rate = 5
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your projected savings after one year, with interest, is:", "$",projected_savings)

