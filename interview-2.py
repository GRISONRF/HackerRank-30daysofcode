#Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.


def plusMinus(arr):
    # Write your code here
    
    # intput -> [1, 1, 0, -1, -1]
    
    positive = 0
    negative = 0
    zero = 0
    length = len(arr)
    
    for num in arr:
        if num > 0:
            positive += 1
        elif num == 0:
            zero += 1
        else:
            negative += 1
    
            
    #positive = 2 / negative = 2 / zero = 1
    
    print("{0:.6f}".format(positive / length))
    print("{0:.6f}".format(negative/ length))
    print("{0:.6f}".format(zero/length))