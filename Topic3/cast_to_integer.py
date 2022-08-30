"""
Program: cast_to_integer.py
Author: Alex Heinrichs
Last date modified: 08/30/2022

The purpose of this program is to accept any input,
convert to a integer type and output the integer.
"""

# This line takes user input with a printed message explaining
# What it will attempt to do (cast to integer)
# First however, since any floating number will be of type string
# a float cast is placed on the input to catch any floating numbers
user_input = float(input('Please type any input'
                         'to be casted into an integer: '))

# this statement casts user_input to an integer and prints it
print(int(user_input))
