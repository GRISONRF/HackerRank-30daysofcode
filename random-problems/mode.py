""" //Write a method called mode that returns the most frequently occurring element of an array of integers.
// Assume that the array has at least one element and that every element in the array has a value between
// 0 and 100 inclusive. Break ties by choosing the lower value.
"""


def mode(lst):
    
    counter = {}

    for i in lst:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    
    return max(counter, key = lambda k: counter[k])


print(mode([27, 15, 15, 11, 27]))