"""
Program: variable_assignment.py
Author: Alex Heinrichs
Last date modified: 08/30/2022

This program's purpose is simply to create three variables and
a constant variable and then print them out
"""

PRICE = 10.99  # creating constant variable for price

quantity = 5  # quantity of item
item = 'hats'  # name of item
size = 9.4  # size of item

# variables are now printed
# Here, quantity, size, and PRICE are all
# needed to be converted into a string using str()
# before they work in a print statement
print(str(quantity) + ' ' + item + ' size ' + str(size))
print(item + ' are ' + str(PRICE))
