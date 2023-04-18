""" Binary search is one of the most important Computer Science algorithms.
    It allows you to search a sorted list in O(log n) time, a large improvement over scanning every item in the list (which would be O(n) time).
To do this, you examine the middle item and, if the sought-for value is smaller, move halfway to the left.
    If the sought-after value is larger, move halfway to the right.
In this challenge, you’ll make binary search for the classic children’s guessing game of “pick a number from 1 to 100”.

Since you use binary search, it will never take more than 7 guesses for a function to find a number in the range 1 to 100
    (since log2 100) is just a little under 7).

For Example:
binarySearch(50) => 1
binarySearch(25) => 2
binarySearch(75) => 2
binarySearch(31) <= 7 => true """

def binary(num):

    #take the range of numbers and devide the lowest and greatest by 2: that's the binary result.
    #how many divisions I'll make to get to the paramether number

    low = 0
    high = 101

    bin = (high + low) / 2   #bin = 50 // 
    counter = 1


    while num != bin:

        if num < bin:
            low = bin
        else:
            high = bin       
        bin = (low + high) / 2
        counter += 1

    return counter






print(binary(50))
print(binary(25))
print(binary(75))
print(binary(31))

