import math 
import numpy as np

start_salary = float(input('Enter the start salary: '))

semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000.0

head = 0
tail = 10000
count = 0

while(head < tail):
    midle = (head + tail) // 2
    portion_saved = float(midle) /10000

    current_savings = 0.0
    annual_salary = start_salary
    num_months = 0
    count += 1
    
    while(current_savings <= total_cost * portion_down_payment):
        current_savings = current_savings * (1 + r / 12)
        current_savings += annual_salary * portion_saved / 12
        num_months += 1
        if (num_months % 6 == 0):
            annual_salary *= (1 + semi_annual_raise)

    if(num_months > 36):
        if(head != midle):
            head = midle
        else:
            print('It is not possible')
            break
    elif(num_months < 36):
        if(head != midle):
            tail = midle
        else:
            print('Steps in bisection search: ',count)
            print('Best savings rate: ',portion_saved)
            break
    else:
        print('Steps in bisection search: ',count)
        print('Best savings rate: ',portion_saved)
        break


