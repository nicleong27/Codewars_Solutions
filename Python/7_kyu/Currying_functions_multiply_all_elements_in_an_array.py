# To complete this Kata you need to make a function multiplyAll/multiply_all 
# which takes an array of integers as an argument. This function must return 
# another function, which takes a single integer as an argument and returns a 
# new array.

# The returned array should consist of each of the elements from the first array 
# multiplied by the integer.

# Example:

# multiplyAll([1, 2, 3])(2) = [2, 4, 6];
# Here's a nice Youtube video about currying, which might help you if this is 
# new to you.


import numpy as np

def multiply_all(array):
    def multiply_with(num):
        return [n * num for n in array]
    return multiply_with