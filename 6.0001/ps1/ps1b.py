annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(
    input('Enter the percent of your salary to save, as a decimal: '))
monthly_savings = (annual_salary / 12) * portion_saved
print(monthly_savings, "amount is saved each month")

total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Semi annual raise decimal percentage: '))
portion_down_payment = 0.25  # 25%
down_payment = total_cost * portion_down_payment
print(down_payment, "amount required for downpayment")

annual_return = 0.04
current_savings = 0.0
number_of_months = 0

while current_savings < down_payment:
    # Runs until down_payment is achieved. Each iteration is for a month
    current_savings = current_savings + monthly_savings + \
        ((current_savings * annual_return) / 12)
    number_of_months += 1
    print("Amount saved as of", number_of_months, "months is", current_savings)
    # Increment every 6 months
    if number_of_months % 6 == 0 and number_of_months > 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_savings = (annual_salary / 12) * portion_saved

print('Number of months: {}'.format(number_of_months))
