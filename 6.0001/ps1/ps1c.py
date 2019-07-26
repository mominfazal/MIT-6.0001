first_annual_salary = float(input('Enter your annual salary: '))

total_cost = 1000000
print("House cost assumed as ", total_cost)

portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
print(down_payment, "amount required for downpayment")

semi_annual_raise = .07
print("Annual increment rate assumed", semi_annual_raise)
annual_return = 0.04
print("Annual returns rate assumed", annual_return)

epsilon = 100 # This is allowed difference in savings vs downpayment
bisection_search = 0 # Simple counter variable


is_possible = True # To determine if the value is achievable in 3 years
max_portion = 10000 # Assumed as 10000
min_portion = 0 # Assumed as 0
best_portion = max_portion # this variable will be computed for portion_saved

while True:
    bisection_search += 1
    annual_salary = first_annual_salary
    best_portion_saved = best_portion / 10000  # best_portion 1, 5000, 2500, 3750..
    monthly_savings = (annual_salary / 12) * best_portion_saved
    print(monthly_savings, "assumed monthly savings to start")
    current_savings = 0.0
    number_of_months = 0
    while number_of_months <= 36:
        # Assumed achieving the down payment amount in 3 years
        # Runs until down_payment is achieved. Each iteration is for a month
        current_savings = current_savings + monthly_savings + \
            ((current_savings * annual_return) / 12)
        number_of_months += 1
        # print("Amount saved as of", number_of_months, "months is", current_savings)
        # Increment every 6 months
        if number_of_months % 6 == 0 and number_of_months > 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_savings = (annual_salary / 12) * best_portion_saved

    #print('current_savings: {}'.format(current_savings))
    if abs(current_savings - down_payment) <= epsilon:
        break

    if abs(min_portion - max_portion) <= 1:
        # When salary is greater then down payment
        print("max_portion + min_portion // 2, stuck in infinte loop")
        break

    if current_savings > down_payment:
        max_portion = best_portion
    else:
        min_portion = best_portion

    if min_portion >= max_portion:
        print('Not possible to save in 3 years')
        break

    # Change the best portion to be saved, here bisection is performed
    best_portion = (max_portion + min_portion) // 2

print('max_portion:', f'{max_portion}')
print("Required savings rate:", f'{best_portion_saved}')
print("Iteration required:", f'{bisection_search}')
