import numpy as np
import math 
x = input('Enter number x: ')
y = input('Enter number y: ')
ans1 = int(x)**int(y)
ans2 = math.log(int(x),2)
print('X**y = ' + str(ans1))
print('log(x) = ' + str(ans2))
