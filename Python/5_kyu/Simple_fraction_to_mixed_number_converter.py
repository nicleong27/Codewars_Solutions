# Given a string representing a simple fraction x/y, your function must return a 
# string representing the corresponding mixed fraction in the following format:

# [sign]a b/c

# where a is integer part and b/c is irreducible proper fraction. There must be 
# exactly one space between a and b/c. Provide [sign] only if negative 
# (and non zero) and only at the beginning of the number (both integer part and 
# fractional part must be provided absolute).

# If the x/y equals the integer part, return integer part only. If integer part 
# is zero, return the irreducible proper fraction only. In both of these cases, 
# the resulting string must not contain any spaces.

# Division by zero should raise an error (preferably, the standard zero division 
# error of your language).

# Value ranges

# -10 000 000 < x < 10 000 000
# -10 000 000 < y < 10 000 000
# Examples

# Input: 42/9, expected result: 4 2/3.
# Input: 6/3, expedted result: 2.
# Input: 4/6, expected result: 2/3.
# Input: 0/18891, expected result: 0.
# Input: -10/7, expected result: -1 3/7.
# Inputs 0/0 or 3/0 must raise a zero division error.
# Note

# Make sure not to modify the input of your function in-place, it is a bad practice.


import math

def reduce_fractions(num, denom):
    GCD = math.gcd(num, denom)
    numerator = num // GCD
    denominator = denom // GCD
    return numerator, denominator

def mixed_fraction(s):
    numlst = s.split('/')
    
    if numlst[0] == '0' and numlst[1] != '0':
        return '0'
        
    elif abs(int(numlst[0])) < abs(int(numlst[1])):
        numerator, denominator = reduce_fractions(int(numlst[0]), int(numlst[1]))
        
        if int(numlst[0]) < 0 and int(numlst[1]) < 0:
            return str(abs(numerator)) + '/' + str(abs(denominator))
        
        elif int(numlst[0]) > 0 and int(numlst[1]) < 0:
            return str(-numerator) + '/' + str(abs(denominator))

        return str(numerator) + '/' + str(denominator)
    
    if int(numlst[0]) % int(numlst[1]) == 0:
        return str(math.floor(int(numlst[0]) / int(numlst[1])))
        
    else:
        wholenum = math.trunc(int(numlst[0]) / int(numlst[1]))
        remaining_frac_num = abs(int(numlst[0]) - wholenum * int(numlst[1]))
        numerator2, denominator2 = reduce_fractions(remaining_frac_num, abs(int(numlst[1])))
        
        if numerator2 < 0 and denominator2 < 0:
            return str(wholenum) + ' ' + str(abs(numerator2)) + '/' + str(abs(denominator2))
        elif numerator2 > 0 and denominator2 < 0:
            return str(wholenum) + ' ' + str(numerator2) + '/' + str(abs(denominator2))

        return str(wholenum) + ' ' + str(abs(numerator2)) + '/' + str(abs(denominator2))