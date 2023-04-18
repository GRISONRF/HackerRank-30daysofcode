"""  We have a two-dimensional board game involving snakes. 
The board has two types of squares on it: +'s represent impassable squares where snakes cannot go, and 0's represent squares through which snakes can move. 
Snakes can only enter on the edges of the board, and each snake can move in only one direction.
We'd like to find the places where a snake can pass through the entire board, moving in a straight line.

Here is an example board:

col-->        0  1  2  3  4  5  6
           +----------------------
row      0 |  +  +  +  0  +  0  0
 |       1 |  0  0  0  0  0  0  0
 |       2 |  0  0  +  0  0  0  0
 v       3 |  0  0  0  0  +  0  0
         4 |  +  +  +  0  0  0  +
Write a function that takes a rectangular board with only +'s and 0's, and returns two collections:

one containing all of the row numbers whose row is completely passable by snakes, and
the other containing all of the column numbers where the column is completely passable by snakes.
Complexity Analysis:

r: number of rows in the board c: number of columns in the board

straightBoard1 = [['+', '+', '+', '0', '+', '0', '0'],
                  ['0', '0', '0', '0', '0', '0', '0'],
                  ['0', '0', '+', '0', '0', '0', '0'],
                  ['0', '0', '0', '0', '+', '0', '0'],
                  ['+', '+', '+', '0', '0', '0', '+']]

findPassableLanes(straightBoard1) // = Rows: [1], Columns: [3, 5]

straightBoard2 = [['+', '+', '+', '0', '+', '0', '0'],
                  ['0', '0', '0', '0', '0', '+', '0'],
                  ['0', '0', '+', '0', '0', '0', '0'],
                  ['0', '0', '0', '0', '+', '0', '0'],
                  ['+', '+', '+', '0', '0', '0', '+']]

findPassableLanes(straightBoard2) // = Rows: [], Columns: [3]

straightBoard3 = [['+', '+', '+', '0', '+', '0', '0'],
                  ['0', '0', '0', '0', '0', '0', '0'],
                  ['0', '0', '+', '+', '0', '+', '0'],
                  ['0', '0', '0', '0', '+', '0', '0'],
                  ['+', '+', '+', '0', '0', '0', '+']]

findPassableLanes(straightBoard3) // = Rows: [1], Columns: []

straightBoard4 = [['+']]
findPassableLanes(straightBoard4) // = Rows: [], Columns: [] """


def findPassableLanes(board):

    rows = []
    for r in range(len(board)):
        all_zeros = True
        for c in range(len(board[0])):

            if board[r][c] == '+':
                all_zeros = False
                break
            
        if all_zeros:
            rows.append(r)
        
    cols = []
    for c in range(len(board[0])):
        all_zero = True
        for r in range(len(board)):
            
            if board[r][c] == '+':
                all_zero = False
                break

        if all_zero:
            cols.append(c)

    print(f'Rows: {rows}, Columns: {cols}')


                



straightBoard1 = [['+', '+', '+', '0', '+', '0', '0'],
                  ['0', '0', '0', '0', '0', '0', '0'],
                  ['0', '0', '+', '0', '0', '0', '0'],
                  ['0', '0', '0', '0', '+', '0', '0'],
                  ['+', '+', '+', '0', '0', '0', '+']]

findPassableLanes(straightBoard1) # = Rows: [1], Columns: [3, 5]

straightBoard2 = [['+', '+', '+', '0', '+', '0', '0'],
                  ['0', '0', '0', '0', '0', '+', '0'],
                  ['0', '0', '+', '0', '0', '0', '0'],
                  ['0', '0', '0', '0', '+', '0', '0'],
                  ['+', '+', '+', '0', '0', '0', '+']]

findPassableLanes(straightBoard2) # = Rows: [], Columns: [3]

straightBoard3 = [['+', '+', '+', '0', '+', '0', '0'],
                  ['0', '0', '0', '0', '0', '0', '0'],
                  ['0', '0', '+', '+', '0', '+', '0'],
                  ['0', '0', '0', '0', '+', '0', '0'],
                  ['+', '+', '+', '0', '0', '0', '+']]

findPassableLanes(straightBoard3) # = Rows: [1], Columns: []

straightBoard4 = [['+']]
findPassableLanes(straightBoard4) # = Rows: [], Columns: []


# def findPassableLanes(board):

#     #find where all rows are 0 and all col are 0

#    #initialize list for rows and cols
#     rows = []  #0, 0, 0, 0, 0
#     cols = []

#     #important to note: the rows and col dont have the same len!

#     #go over the rows
#     for r in range(len(board)):
#         # initialize it as true
#         row_all_zeros = True
#         #go over the cols
#         for c in range(len(board[0])):
            
#             #if it's a +, change it to false and break
#             if board[r][c] == '+':
#                 row_all_zeros = False
#                 break
        
#         #check if it's true, if it is append the row number to rows
#         if row_all_zeros:
#             rows.append(r)


#     #now we want to check for the cols.
#     #so first iterate over cols
#     for c in range(len(board[0])):
#         #itiliaize it to true
#         col_all_zeros = True
#         #go over the rows
#         for r in range(len(board)):

#             #check if its a +, if it is change it to false and break
#             if board[r][c] == '+':
#                 col_all_zeros = False
#                 break
#         #if  it's true, add the col number to the cols
#         if col_all_zeros:
#             cols.append(c)
        
        

#     print(f'Rows: {rows}, Columns: {cols}')