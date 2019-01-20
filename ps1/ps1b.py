import math 
import numpy as np

annual_salary = float(input('Enter your annual salary: '))
portion_saved = input('Enter the percent of your salary to save, as a decimal: ')
portion_saved = float(str('0') + portion_saved )
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = input('Enther the semi-annual reaise,as a decimal: ')
semi_annual_raise = float(str('0') + semi_annual_raise)


current_savings = 0.0
portion_down_payment = 0.25
r = 0.04
num_months = 0



while(current_savings <= total_cost * portion_down_payment):
    current_savings = current_savings * (1 + r / 12)
    current_savings += annual_salary * portion_saved / 12
    num_months += 1
    if (num_months % 6 == 0):
        annual_salary *= (1 + semi_annual_raise)


print('Number of months: ', num_months)