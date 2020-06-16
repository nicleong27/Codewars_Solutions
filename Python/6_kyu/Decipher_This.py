# You are given a secret message you need to decipher. Here are the things 
# you need to know to decipher it:

# For each word:

# the second and the last letter is switched (e.g. Hello becomes Holle)
# the first letter is replaced by its character code (e.g. H becomes 72)
# Note: there are no special characters used, only letters and spaces

# Examples

# decipherThis('72olle 103doo 100ya'); // 'Hello good day'
# decipherThis('82yade 115te 103o'); // 'Ready set go'


def decipher_this(string):
    str_split = string.split()
    
    first_letters = []
    
    for word in str_split:
        first_letter = ''
        for char in word:
            if char.isdigit():
                first_letter += char
        first_letters.append(chr(int(first_letter)))
    
    letters = []
    
    for word in str_split:
        other_letters = ''
        for char in word:
            if not char.isdigit():
                other_letters += char
        letters.append(other_letters)
    
    final = [i + j for i, j in zip(first_letters, letters)]
    
    output = []
    
    for word in final:
        if len(word) > 2:
            word = list(word)
            word[1], word[-1] = word[-1], word[1]
            output.append(''.join(word))
        else:
            output.append(word)
            
    return ' '.join(output)