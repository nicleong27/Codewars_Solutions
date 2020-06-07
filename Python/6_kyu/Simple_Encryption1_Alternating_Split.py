# For building the encrypted string:
# Take every 2nd char from the string, then the other chars, that are not every 
# 2nd char, and concat them as new String.
# Do this n times!

# Examples:

# "This is a test!", 1 -> "hsi  etTi sats!"
# "This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
# Write two methods:

# def encrypt(text, n)
# def decrypt(encrypted_text, n)
# For both methods:
# If the input-string is null or empty return exactly this value!
# If n is <= 0 then return the input text.

# This kata is part of the Simple Encryption Series:
# Simple Encryption #1 - Alternating Split
# Simple Encryption #2 - Index-Difference
# Simple Encryption #3 - Turn The Bits Around
# Simple Encryption #4 - Qwerty

# Have fun coding it and please don't forget to vote and rank this kata! :-)


def decrypt(encrypted_text, n):
    if n <= 0 or encrypted_text == '' or encrypted_text == None:
        return encrypted_text
            
    evens = ''
    odds = ''
    middle = len(encrypted_text) // 2
    original_s = encrypted_text
    second_half2 = encrypted_text[middle:]
    
    for i in range(n):
        s = ''
        first_half = original_s[:middle]
        second_half = original_s[middle:]
        for i in range(middle):
            s += second_half[i] + first_half[i]
        original_s = s
        
    if len(encrypted_text) % 2 != 0:
        original_s += second_half2[middle]
        
    return original_s



def encrypt(text, n):
    if n <= 0 or text == '' or text == None:
        return text
    
    for i in range(n):
        evens = ''
        odds = ''
        for j in range(len(text)):
            if (j+1) % 2 == 0:
                evens += text[j]
            else:
                odds += text[j]
        text = evens + odds

    return text