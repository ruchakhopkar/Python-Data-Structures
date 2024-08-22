# Implement a Python function called print_items.
# This function should take a single integer as an argument and print out a sequence of numbers from 0 up to, but not including, the provided integer.
# The function should use a for loop and Python's built-in range function to generate the sequence of numbers.
# The function signature should be: def print_items(n):

## WRITE THE PRINT_ITEMS FUNCTION HERE ##
def print_items(n):
    for i in range(n):
        print(i)
       
# DO NOT CHANGE THIS LINE:
print_items(10)
