""" there is an image filled with 0s and 1s. There is at most one rectangle in this image filled with 0s, find the rectangle. 
Output could be the coordinates of top-left and bottom-right elements of the rectangle, or top-left element, width and height.

 """

            
def find_one_rectangle(board):

    #ans = [] -store coordinates

    #iterate over row
        #iterate over col
            #if curr element == 0:  -> means its the top-left of rectangle, add (r,c) to ans
                #row
                #while on bounds and the item in next row == 0:
                    #r+=1
                #col
                #while on bounds and the item in next col == 0:
                    #c+=1
                #when break the while loops, the coordinates from r and c = bottom right
                #add coordinates to ans
    
    ans = []
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                ans.append((r,c))
                
                h = r
                while h+1 < len(board) and board[h+1][c] == 0:
                    h+=1
                
                while c+1 < len(board[0]) and board[r][c+1] == 0:
                    c+=1
                
                ans.append((h,c))
                return ans
                
    print(ans)




print(find_one_rectangle([
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1],   #r2, c3) (3,5)
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
]))



print(find_one_rectangle([
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 0, 0, 0, 1],
[1, 0, 1, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1],
[1, 0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1]
]))#Expected output: (2,3), (3,5)


print(find_one_rectangle([
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 0, 0, 0, 1, 1]
])) #Expected output: (7,3), (7,5)

print(find_one_rectangle([
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
])) #Expected output: (0,0), (7,7)



""" def find_one_rectangle(board):

         
    if not board:
            return []

    result = []
    #go over the rows
    for i in range(len(board)):
        #over columns
        for j in range(len(board[0])):
            #if at that point of the board is a 0
            if board[i][j] == 0:
                #append the coordinates into the result -> coordinates of the top-left -> start of the rectangle
                result.append((i, j))
                #initialize height and width as 1 (because so far we only found one 0)
                height, width = 1, 1
                #checking the height:
                # the height is what keeps incrementing by 1, which means when i + height is on bound and if the next number going down (column doesnt change) is 0, increment height. same thing with width, where the row does not change
                while i + height < len(board) and board[i + height][j] == 0:
                    height += 1
                while j + width < len(board[0]) and board[i][j + width] == 0:
                    width += 1
                #at the end, we will append to the result the coordinates to the bottom right of the rectangle: 
                result.append((i + height - 1, j + width - 1))
                return result
    return [] """



