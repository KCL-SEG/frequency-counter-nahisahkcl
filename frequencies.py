"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        if str(item) not in frequencies.keys():
            frequencies[str(item)] = items.count(str(item)


    return frequencies

print(frequencies(['0', 4,4,'4','d','d','e',0,'a','d','4']))
