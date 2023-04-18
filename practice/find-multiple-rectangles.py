""" PREVIOUS QUESTION: there is an image filled with 0s and 1s. There is at most one rectangle in this image filled with 0s, find the rectangle. 
Output could be the coordinates of top-left and bottom-right elements of the rectangle, or top-left element, width and height.

THIS QUESTION:for the same image, it is filled with 0s and 1s. It may have multiple rectangles filled with 0s.
 The rectangles are separated by 1s. Find all the rectangles.

"""

def find_rectangles(board):

    ans = []
    for r in range(len(board)):
        for c in range(len(board[0])):
            

            if board[r][c] == 0:
                temp_rec = [(r,c)]
                board[r][c] = 1 #mark as visited, so we dont count it again

                h = r
                while h+1 < len(board) and board[h+1][c] ==0:
                    h+=1

                w = c    
                while w+1 < len(board[0]) and board[r][w+1] ==0:
                    w+=1
               
                #set all r and c as visited (to 1)
                for row in range(h-r+1):
                    for col in range(w-c+1):
                        board[r+row][c+col]=1
                temp_rec.append((h,w))
                ans.append(temp_rec)
               
    print(ans)



print(find_rectangles([
    [1, 1, 1, 1, 1, 1, 1],  
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1],   #r2, c3) (3,5)
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
]))



print(find_rectangles([
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 0, 0, 0, 1],
[1, 0, 1, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1],
[1, 0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1]
]))#Expected output: (2,3), (3,5) [3,1)(5,1)] [(5,3)(6,6)]


print(find_rectangles([
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 0, 0, 0, 1, 1]
])) #Expected output: (7,3), (7,5)

print(find_rectangles([
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
])) #Expected output: (0,0), (7,7)
