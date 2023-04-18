""" You are creating Flippy, an AT that plans to take over the world by solving games having to do with flipping things. First the Al must master a one-dimensional game called Reversi


There are two players, denoted by 'X' (the AI player) and 'O'.The goal is to place a new X in a blank space on the board to capture the O' tokens between two 'X* tokens (with no spaces in between). 
A move can capture to the left or the right, not both, of the newly laced 'X

the valid moves in this example are 4, 5 and 13 (the blank spaces)

0   1   2   3   4   5   6   7   8   9   10   11   12   13
X   O   O   O   ''  ''  O   O   X   O    X    X    O   ''
* move at 13 (flips 12)
* move at 4 <---- x (flips 1, 2 and 3)
* move at 5           x ---------> (flips 6 and 7)

The optimal move captures as many 'O' as possible. In this case, that move is 4, which captures tree tokens

write a function that, given a board, returns the optimal move for 'X', together with how many tokens are captured 

RETURN INDEX OF FLIP AND HOW MANY CAPTURES"""

# find the spaces
# put an 'X' in them
# change into X from one X to another X and keep track of index of them
# return the largest capture 

# find the first X. store it's index (and create a count)
# find the next X or empty space.
    # if an X: check if the counter of captures is greater than current one


#['X', 'O', 'z', 'O', 'O', 'O'] 

def flippy(board):

    result = [0,0] #index, count

    #we iterate until the len-1 beause since we're comparing to the next element, if we don't do this, we will get an index error
    for i in range(len(board) -1):

        #if curr is an X and the next is an O, want to keep track of how many O's are after the X:
        if board[i] == 'X' and board[i + 1] == 'O':

            count = 0
            #while we have Os after the X, update counter 
            while board[i + 1] == 'O' and i+1 < len(board)-1:
                count+=1
                i+=1
            #when there's no more O's, 
            #if its an 'z':
            if board[i+1] == 'z':
                #update result
                max_flips = max(result[1], count)
                result[0], result[1] = i+1, max_flips
            

        #if curr = ' ' 
        elif board[i] == 'z' and board[i+1] == 'O':

            count = 0
            while board[1+i] == 'O' and i+1 < len(board) - 1:
                count+=1
                i+=1

            if board[i+1] == 'X':
                max_flips = max(result[1], count)
                result[0], result[1] = i - count , max_flips
            
    return result if result != [0,0] else None
            



board = ['z', 'O', 'X'] #0,1
board2 = ['X', 'O', 'z', 'O', 'O', 'O'] #2, 1
board3 = ['X', 'O', 'O', 'z', 'O', 'O', 'O'] #3,2 (if a move captures both left and right we only count the larger of the two captures)
board4 = ['X', 'O', 'X', 'z'] #none/null.
print(flippy(board))
print(flippy(board2))
print(flippy(board3))
print(flippy(board4))


