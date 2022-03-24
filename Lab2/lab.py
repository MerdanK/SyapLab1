from math import*
import math

num_a = float(input('Enter number a: '))
num_b = float(input('Enter number b: '))
 

result = (sin(2*sqrt(num_a**2 + num_b**2 ))*cos(2*sqrt(num_a**2-num_b**2))) / (5*log(1 + 3*num_a + 3*num_b**2));

print('result = ' + str(result));

 
 