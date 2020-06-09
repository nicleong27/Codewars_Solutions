# Suppose we know the process by which a string s was encoded to a string r 
# (see explanation below). The aim of the kata is to decode this string r to 
# get back the original string s.

# Explanation of the encoding process:

# input: a string s composed of lowercase letters from "a" to "z", and a 
# positive integer num
# we know there is a correspondence between abcde...uvwxyzand 0, 1, 2 ..., 
# 23, 24, 25 : 0 <-> a, 1 <-> b ...
# if c is a character of s whose corresponding number is x, apply to x the 
# function f: x-> f(x) = num * x % 26, then find ch the corresponding character 
# of f(x)
# Accumulate all these ch in a string r
# concatenate num and r and return the result

def decode(r):
    num = ''
    letters = ''
    alphs = [chr(i + 97) for i in range(26)]

    for c in r:
        if c.isdigit():
            num += c
        else:
            letters += c
            
    output = ''
    
    s_vals = [chr(97 + i * int(num) % 26) for i in range(26)]
    
    mapped_vals = dict(zip(s_vals, alphs))
        
    if len(mapped_vals) != 26:
        return 'Impossible to decode'
    return ''.join(mapped_vals[l] for l in letters)