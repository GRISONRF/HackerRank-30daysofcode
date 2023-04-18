""" 
While your players are waiting for a game, you've developed a solitaire game for the players to pass the time with.
The player is given an NxM board of tiles from 0 to 9 like this:
4 4 4 4
5 5 5 4
2 5 7 5
The player selects one of these tiles, and that tile will disappear, along with any tiles with the same number that are connected with that tile (up, down, left, or right), and any tiles with the same number connected with those, and so on. 
For example, if the 4 in the upper left corner is selected, these five tiles disappear

4< >4< >4< >4<
5 5 5 >4<
2 5 7 5
If the 5 just below it is selected, these four tiles disappear. Note that tiles are not connected diagonally.
4 4 4 4
5< >5< >5< 4
2 >5< 7 5
Write a function that, given a grid of tiles and a selected row and column of a tile, returns how many tiles will disappear.
grid1 = [[4, 4, 4, 4],
         [5, 5, 5, 4],
         [2, 5, 7, 5]]

disappear(grid1, 0, 0) => 5
disappear(grid1, 1, 1) => 4
disappear(grid1, 1, 0) => 4
This is the grid from above.

Additional Inputs
grid2 = [[0, 3, 3, 3, 3, 3, 3],
         [0, 1, 1, 1, 1, 1, 3],
         [0, 2, 2, 0, 2, 1, 4],
         [0, 1, 2, 2, 2, 1, 3],
         [0, 1, 1, 1, 1, 1, 3],
         [0, 0, 0, 0, 0, 0, 0]]

grid3 = [[0]]

grid4 = [[1, 1, 1],
[1, 1, 1],
[1, 1, 1]]

All Test Cases
disappear(grid1, 0, 0) => 5
disappear(grid1, 1, 1) => 4
disappear(grid1, 1, 0) => 4

disappear(grid2, 0, 0) => 12
disappear(grid2, 3, 0) => 12
disappear(grid2, 1, 1) => 13
disappear(grid2, 2, 2) => 6
disappear(grid2, 0, 3) => 7

disappear(grid3, 0, 0) => 1

disappear(grid4, 0, 0) => 9

N - Width of the grid
M - Height of the grid """


"""
Create a 2D grid to store the visited state of each tile.
Start the DFS from the selected row and column.
Mark the current tile as visited.
If the current tile has the same value as the selected tile, increase the counter by 1 and continue the DFS in all 4 directions (up, down, left, and right).
Repeat steps 3 and 4 for all unvisited tiles with the same value as the selected tile.
Return the final count of the disappeared tiles.

This approach will explore all tiles with the same value as the selected tile and count them in a single DFS, resulting in a solution that is both efficient and effective. """

def disappear(grid, t1, t2):

    #keep track of tile already visited
    visited = []

    #define row, col and the 'target' tile
    row = t1
    col = t2
    tile = grid[t1][t2]
    
    #count how many tiles match the target
    counter = 0

    #dfs function
    def dfs(row, col):

        #if current row is in bounds (greater than 0 and less than the end of grid)
        if row >= 0 and row < len(grid) and col >=0 and col < len(grid[0]):

            #if this row and col have already been visited
            if (row, col) in visited:

                return 
            #if it's in bounds and have NOT been visited, append the row and col to the visited list
            visited.append((row,col))

            #if this current value in the row and col are equal to the target, add 1 to the counter
            if grid[row][col] == tile:
                #since counter was initialized outside of dfs, need to use the nonlocal to reference it
                nonlocal counter
                counter+=1

                #now check all directions of the current tile looking for equal numbers
                #up
                dfs(row-1, col)
                #down
                dfs(row+1, col)
                #left
                dfs(row, col-1)
                #right
                dfs(row, col+1)

    #call dfs
    dfs(row, col)
        # return counter
        #at the end return counter
    print(counter)
   



grid1 = [[4, 4, 4, 4],
         [5, 5, 5, 4],
         [2, 5, 7, 5]]

disappear(grid1, 0, 0) # 5

disappear(grid1, 1, 1) # 4
disappear(grid1, 1, 0) # 4

grid2 = [[0, 3, 3, 3, 3, 3, 3],
[0, 1, 1, 1, 1, 1, 3],
[0, 2, 2, 0, 2, 1, 4],
[0, 1, 2, 2, 2, 1, 3],
[0, 1, 1, 1, 1, 1, 3],
[0, 0, 0, 0, 0, 0, 0]]

disappear(grid2, 0, 0) # 12
disappear(grid2, 3, 0) # 12
disappear(grid2, 1, 1) # 13
disappear(grid2, 2, 2) # 6
disappear(grid2, 0, 3) # 7

grid3 = [[0]]

disappear(grid3, 0, 0) # 1

grid4 = [[1, 1, 1],
[1, 1, 1],
[1, 1, 1]]


disappear(grid4, 0, 0) # 9