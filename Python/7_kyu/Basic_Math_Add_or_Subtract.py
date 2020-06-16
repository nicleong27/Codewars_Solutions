# In this kata, you will do addition and subtraction on a given string. 
# The return value must be also a string.

# Note: the input will not be empty.

# Examples

# "1plus2plus3plus4"  --> "10"
# "1plus2plus3minus4" -->  "2"


import ast

def calculate(s):
    new_s = s.replace('plus', '+')
    final = new_s.replace('minus', '-')
    
    return str(ast.literal_eval(final))