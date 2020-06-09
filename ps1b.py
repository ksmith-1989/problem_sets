# annual salary
annual_salary = int(input("Enter annual salary: "))
monthly_salary = annual_salary/12

#ask user for semi annual raise
salary_raise = float(input("Enter a semi annual salary raise as a decimal:"))

# saving 10% each month
portion_saved = float(
    input("Enter how much you will save each month as a decimal: "))
monthly_saved = monthly_salary * portion_saved
# cost of home
total_cost = int(input("Enter the cost of your dream home:"))
# down payment %
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment

# current savings
current_savings = 0

# investments earn 4%
r = 0.04

ror = r/12

months = 0


while current_savings < down_payment:
    months += 1
    current_savings *= 1 + ror
    current_savings += monthly_saved
    if months % 6 == 0:
        annual_salary = (annual_salary * salary_raise) + annual_salary
        monthly_salary = annual_salary/12
        monthly_saved = monthly_salary * portion_saved




print('Number of months:', months)