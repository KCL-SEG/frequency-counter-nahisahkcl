"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        if item not in frequencies.keys():
            frequencies[item] = items.count(item)


    return frequencies
