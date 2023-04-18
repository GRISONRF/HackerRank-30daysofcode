""" Matrix Validation
Given a N*N matrix, determine if it is a valid matrix. 

A valid matrix is defined as each row or each column having exactly the numbers 1 to N. Output a boolean 

*no duplicates in a row
no duplicates in a column

row = matrix[ROW][j]
column = matrix[i][COLUMN]

-> check if matrix is not null and has dimentions N*N, if not return false
-> iterate over each row and column and use sets to store the elements
-> for each row: check if every element is unique, if the max and min are 1 and N. if not return false
-> for each column: check if every element is unique, if the max and min are 1 and N. if not return false
-> if row and column passed the test, return true

"""

def isValidMatrix(matrix):

   

    #check if matrix is empty and N*N
    if not matrix or len(matrix) != len(matrix[0]):
        return False

    #iterate over rows
    for row in range(len(matrix)):

        #create set for elements
        row_set = set()
        col_set = set()
        #initialize the min and max for elements   -> since each row needs to have numbers from 1 to N, at the end we will check if the min = 1 and the max = length of the matrix(N)
        row_min, row_max = float('inf'), float('-inf')  
        col_min, col_max = row_min, row_max
        
        #iterate over cols
        for col in range(len(matrix[0])):
            #start checking for duplicates in every row
            #if this row and col are NOT already in the row set
            if matrix[row][col] not in row_set:
                # add them in the row set 
                row_set.add(matrix[row][col])
                #update row min = rowmin, this matrix
                row_max = max(row_max, matrix[row][col])
                #update row max = rowmax, this matrix
                row_min = min(row_min, matrix[row][col])
            #else
            else:
                # return false
                return False
            # if this col and row are NOT in the col set
            if matrix[col][row] not in col_set:
                #add them in the col set
                col_set.add(matrix[col][row])
                #update col min = colmin, this matrix
                col_max = max(col_max, matrix[col][row])
                #update col max = colmax, this matrix
                col_min = min(col_min, matrix[col][row])
            #else
            else:
                #return false
                return False
        # if rowmin != 1 or colmin != 1 or rowmax != len of matrix or colmax != len of matrix
        if row_min != 1 or col_min != 1 or row_max != len(matrix) or col_max != len(matrix):
            return False
            #return false
    #return true        
    return True
          

    # print(set)
            # if row 
            


# valis matrix
matrix = [[1, 2, 3], [2, 3, 1], [3, 1, 2]] #true

# Test case 2: Invalid matrix (duplicate elements in row)
matrix2 = [[1, 2, 3], [2, 3, 2], [3, 1, 2]] #false

# Test case 3: Invalid matrix (duplicate elements in column)
matrix3 = [[1, 2, 3], [2, 1, 2], [3, 1, 2]] #false

# Test case 4: Invalid matrix (element out of range)
matrix4 = [
    [1, 2, 3], 
    [2, 3, 4], 
    [3, 1, 2]] #false

matrix5 = [] #false

print(isValidMatrix(matrix))
print(isValidMatrix(matrix2))
print(isValidMatrix(matrix3))
print(isValidMatrix(matrix4))
print(isValidMatrix(matrix5))
