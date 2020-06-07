# This kata focuses on the Numpy python package and you can read up on the Numpy 
# array manipulation functions here: 
# https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.array-manipulation.html

# You will get two integers N and M. You must return an array with 
# two sub-arrays with numbers in ranges [0, N / 2) and [N / 2, N) respectively, 
# each of them being rotated M times.

import numpy as np

def reorder(a, b):
    first_array = list(np.arange(a // 2))
    second_array = list(np.arange(a // 2, a))
    
    output = [list(np.roll(first_array, b)), list(np.roll(second_array, b))]
    
    return output