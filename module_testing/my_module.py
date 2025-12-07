#Simple custom module with an add function

def add(a, b):
    return a + b




#------------------------------------------------------------------------------------
# Test the function when the module is run directly => use to test module functionalities 
if __name__ == "__main__": # This block will only run if this file is executed directly (name equals main)
    print("Testing addition module.")
    print(f"Example: add(2, 3) = {add(2, 3)}")  #Output: Example: add(2, 3) = 5
    print(f"Example: add(-1, 1) = {add(-1, 1)}")  #Output: Example: add(-1, 1) = 0