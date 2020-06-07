
# Your task is to add up letters to one letter.

# The function will be given a variable amount of arguments, 
# each one being a letter to add.

# Notes:

# Letters will always be lowercase.
# Letters can overflow (see second to last example of the description)
# If no letters are given, the function should return 'z'
# Examples:

# add_letters('a', 'b', 'c') = 'f'
# add_letters('a', 'b') = 'c'
# add_letters('z') = 'z'
# add_letters('z', 'a') = 'a'
# add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
# add_letters() = 'z'

def add_letters(*letters):
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
          'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
          'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
          't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}


    total = sum([d[letter] for letter in letters])
    
    if total > 26:
        total = total % 26
        
    for key, val in d.items():
        if total == val:
            return key
    return 'z'