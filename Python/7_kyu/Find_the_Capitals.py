# Write a method that takes a sequence of objects with two keys each: country or 
# state, and capital. Keys may be symbols or strings

# The method should return an array of sentences declaring the state or country 
# and its capital.

# Examples
# Python

# [{'state': 'Maine', 'capital': 'Augusta'}] --> ["The capital of Maine is Augusta"]
# [{'country' : 'Spain', 'capital' : 'Madrid'}] --> ["The capital of Spain is Madrid"]
# [{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', 
# "capital" : "Madrid"}] --> ["The capital of Maine is Augusta", "The capital of Spain is Madrid"]


def capital(capitals): 
    names = []
    output = []
    
    for row in capitals:
        lst = []
        for key, val in row.items():
            lst.append(val)
        names.append(lst)
    
    for row in names:
        output.append('The capital of {} is {}'.format(row[0], row[1]))
      
    return output