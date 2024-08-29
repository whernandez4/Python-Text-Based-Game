print('')
print('*******Paycheck Calculator Test. Copyright by WALT INDUSTRIES 08/15/2024*******')
print('')
print('Welcome! The following program is intended to assist with calculating', end=' ')
print('a periodic paycheck. Please download the app for quick acess and advance features.')
print('')

salary = float(input("What is your Hourly salary? "))
hours = int(input("How many hours did you work? "))
overtime = int(input("How many hours of overtime did you perform? "))
overtime_salary = (salary / 2 + salary) * overtime
gross_income = salary * hours + overtime_salary

print('')
print("Your pay for the period is:", gross_income)
print('')
print('Would you like to continue to subtract tax? Enter Y for yes or N to quit.')
print('')

user_answer1 = str(input())

if (user_answer1 == 'y') or (user_answer1 == 'Y'):
    print()
    print('Please enter your tax percentage rate.')
    print('')
else:
    print('Cheers!')
    quit()

user_answer2 = float(input())
net_income = gross_income

print('')
print('Your paycheck after taxes is', net_income)
