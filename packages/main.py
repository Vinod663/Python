# import my_calculator.addition as add
# import my_calculator.subtraction as sub

# result_add = add.add(10, 5)
# print(f"The addition result is = {result_add}") 

# result_sub = sub.subtract(10, 5)
# print(f"The subtraction result is = {result_sub}")  


#----------------------------------------------------------------------------------------------------------------------------
# #without aliasing
# import my_calculator.addition
# import my_calculator.subtraction

# result_add = my_calculator.addition.add(10, 5)
# result_sub = my_calculator.subtraction.subtract(10, 5)

# print(f"The addition result is = {result_add}")
# print(f"The subtraction result is = {result_sub}")


#----------------------------------------------------------------------------------------------------------------------------
# #using from-import -1
# from my_calculator import addition, subtraction

# result_add = addition.add(10, 5)
# result_sub = subtraction.subtract(10, 5)

# print(f"The addition result is = {result_add}")
# print(f"The subtraction result is = {result_sub}")




#----------------------------------------------------------------------------------------------------------------------------
#using from-2  => import to directly import functions
# from my_calculator.addition import add
# from my_calculator.subtraction import subtract

# result_add = add(10, 5)
# print(f"The addition result is = {result_add}")

# result_sub = subtract(10, 5)
# print(f"The subtraction result is = {result_sub}")



#----------------------------------------------------------------------------------------------------------------------------
#using init file of package using from-import
from my_calculator import add, subtract

result_add = add(10, 5)
print(f"The addition result is = {result_add}")

result_sub = subtract(10, 5)
print(f"The subtraction result is = {result_sub}")


