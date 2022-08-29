""" We define a magic square to be an  matrix of distinct positive integers from  to  where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.
You will be given a  matrix  of integers in the inclusive range . We can convert any digit  to any other digit  in the range  at cost of . Given , convert it into a magic square at minimal cost. Print this cost on a new line.
Note: The resulting magic square must contain distinct integers in the inclusive range . """



import sys 
def formingMagicSquare(s):

    #convert a 2d matrix to a 1d matrix
    s = sum(s, []) #it 

    #get a magic square 3x3 from 1 to 9 on google
    magic = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4], [4, 9, 2, 3, 5, 7, 8, 1, 6], [2, 9, 4, 7, 5, 3, 6, 1, 8], [8, 3, 4, 1, 5, 9, 6, 7, 2], [4, 3, 8, 9, 5, 1, 2, 7, 6], [6, 7, 2, 1, 5, 9, 8, 3, 4], [2, 7, 6, 9, 5, 1, 4, 3, 8]]

    # compare s to the possibilities in magic to find which one has the mininum cost. So I'll have to calculate the cost and store somewhere, to at the end, i'll return the minimum one.

    # initialize the minimumcost as the largest interger suported by ""python""/// using sys.maxsize or float("inf") // because at the end we use this to store the minimum cost after comparing all of the costs in diff, so it has to be a very large number, otherwise it might return minimuncost instead of diff.
    minimuncost = sys.maxsize
    
    #iterate through the magic and see if s = each array.
    for mag in magic:
        diff = 0
        for i, m in zip(s, mag):  # creating tuples with same index number from each array and checking the difference of each one
            diff += abs(i-m)
        print(diff)
        minimuncost = min(minimuncost, diff)
        
    return minimuncost



print(formingMagicSquare([[5, 3, 4], [1, 5, 8], [6, 4, 2]]))