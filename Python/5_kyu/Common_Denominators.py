# Common denominators

# You will have a list of rationals in the form

#  { {numer_1, denom_1} , ... {numer_n, denom_n} } 
# or

#  [ [numer_1, denom_1] , ... [numer_n, denom_n] ] 
# or

#  [ (numer_1, denom_1) , ... (numer_n, denom_n) ] 
# where all numbers are positive ints.

# You have to produce a result in the form

#  (N_1, D) ... (N_n, D) 
# or

#  [ [N_1, D] ... [N_n, D] ] 
# or

#  [ (N_1', D) , ... (N_n, D) ] 
# or

# {{N_1, D} ... {N_n, D}} 
# or

# "(N_1, D) ... (N_n, D)"
# depending on the language (See Example tests)

# in which D is as small as possible and

#  N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.
# Example:

# convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]
# Note:

# Due to the fact that first translations were written long ago - more than 
# 4 years - these translations have only irreducible fractions. Newer translations 
# have some reducible fractions. To be on the safe side it is better to do a bit 
# more work by simplifying fractions even if they don't have to be.

# Note for Bash:

# input is a string, e.g "2,4,2,6,2,8"

# output is then "6 12 4 12 3 12"


import math
import numpy as np

def lcm(arr):
    lcm = arr[0]
    
    for i in range(1, len(arr)):
        lcm = lcm * arr[i] // math.gcd(lcm, arr[i])
    return lcm

def convertFracts(lst):
    if lst == []:
        return []
        
    denoms = [row[1] for row in lst]
    LCM = lcm(denoms)
    final_denoms = [1 * LCM for  i in range(len(lst))]
    
    numerators = [row[0] * (LCM // row[1]) for row in lst]
    output = [list(tup) for tup in list(zip(numerators, final_denoms))]
    
    return output