#import my_module as md #==> aliasing 

#result = md.add(5, 3)

from my_module import add #importing specific function without aliasing
from math import factorial, sqrt #importing multiple functions from math module

#from math import * #importing all functions from math module==> not recommended due to namespace pollution

sqrt_result = sqrt(16) #using sqrt function from math module
print(f"The square root of 16 is = {sqrt_result}")  #Output: The square root of 16 is = 4.0

factorial_result = factorial(5) #using factorial function from math module
print(f"The factorial of 5 is = {factorial_result}")  #Output: The factorial of 5 is = 120

result = add(5, 3) #calling the function directly without aliasing
print(f"The sum is = {result}")  #Output: The sum is = 8