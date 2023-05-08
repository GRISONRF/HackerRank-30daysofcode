""" 
A grid of characters is given, we can move only one step right or one step down from current position,
Suppose you are at ( i, j ), we can go to either ( i, j+1 ) or ( i+1, j)
char[][] grid1 = {
   0    1    2    3    4    5
0{'c', 'c', 'x', 't', 'i', 'b'},
1{'c', 'c', 'a', 't', 'n', 'i'},
2{'a', 'c', 'n', 'n', 't', 't'},
3{'t', 'c', 's', 'i', 'p', 't'},
4{'a', 'o', 'o', 'o', 'a', 'a'},
5{'o', 'a', 'a', 'a', 'o', 'o'},
6{'k', 'a', 'i', 'c', 'k', 'i'}
};  -> [(1,1)(1,2)(1,3)(2,3)(3,3)(3,4)]


Given a string, we need to find out of the coordinates of the string from start to end if it exists in the grid;
class Coordinate {
    int x, y;

    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

DFS algorith that traverses the grid and backtracks whenever the current character does not match the next character in word

create a function with 2 arguments: 'grid' and 'word' to search for
initialize a 'visited' matrix the same size as the original grid to keep track of visited cells during the search
define helper function to 'is_valid()' to check if a given cell (x,y) is within the bounds of the grid and hasn't been visited

DFS function: takes the current cell coordinates (x,y) and the index 'idx' of the next character to match in the word.
if the 'idx' reaches the length of the word, it means we found a match and return 'TRUE'. otherwise, check if the currect cell is valid and its character matches the currenct character in the word. if so, mark the cell as visited and recursivelly call 'DFS()' on its unvisited neighbors '(x, y+1)' and '(x+1, y)'. if either of these recursive calls returns 'TRUE', we have found a match and we append the current cell coordinates to the 'coordinates' list in reverse order (since we backtracked from the end to the beginning)

we iterate over all cells in the grid and call 'DFS()' on each one. if a match is foung, we return the 'coordinates' list in reverse order. otherwise return 'NONE'


-> 



"""

#defines a coordinate class that has two instance variables 'x' and 'y'. and an '__init__' that initializes these variables
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#function to find the coordinates. takes the grid and word as arguments
def find_coordinates(grid, word):
    #m = row, n = col. they are the same size of r and c of original grid
    m, n = len(grid), len(grid[0])
    #creates a grid called visited the same size as original grid and mark every cell as FALSE
    visited = [[False] * n for _ in range(m)] #[[False for c in range(cols)] for r in range(rows)]

    #func to check if it's a valid coordinate
        #valid if: x is row, so it needs to be greater or equal to 0(starting point in grid) and less than the len of row(end of grid). same for y. AND check if they are NOT visited (if that point in visited is not true)
    def is_valid(x, y):
        return x >= 0 and x < m and y >= 0 and y < n and not visited[x][y]


    #start of dfs. takes the x(row), y(col) and index of current char in word being searched for
    def dfs(x, y, idx):
        #if the index is equal to the len or word, means this is the last char, so we found the word and return True
        if idx == len(word):
            return True

        # if coordinates are valid and the grid at these coordinates are the same char as the char at word that we're seacrching for, we mark this coordinates in visited as 'TRUE' and set the neighbors [to the right and down the current coordinate]    
        if is_valid(x, y) and grid[x][y] == word[idx]:
            visited[x][y] = True
            neighbors = [(x, y+1), (x+1, y)]

            #do a DFS in the neighbors
            for nx, ny in neighbors:   #check y+1 first, then x+1
                if dfs(nx, ny, idx+1):   #if the DFS returns TRUE (means the WORD has been found)
                    coordinates.append((x, y))  #create a Coordinate object using the x and y values and appending to coodinates list. 
                    return True   #return true indicating the word has been found
            visited[x][y] = False
        return False

    coordinates = []
    #this is the DFS call. we're calling it at every cell in the grid, starting at 0 always. if the word is in there, it will return true, so we can return the coordinates in reverse order.
    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return coordinates[::-1] # reversing the list to get the correct order
    return None

grid = [['c', 'c', 'x', 't', 'i', 'b'],
        ['c', 'c', 'a', 't', 'n', 'i'],
        ['a', 'c', 'n', 'n', 't', 't'],
        ['t', 'c', 's', 'i', 'p', 't'],
        ['a', 'o', 'o', 'o', 'a', 'a'],
        ['o', 'a', 'a', 'a', 'o', 'o'],
        ['k', 'a', 'i', 'c', 'k', 'i']]
        
word = "catnip"
print(find_coordinates(grid, word))

## T:  loop to create grid / recursion / loop to correct order = O(mn*3^l) where m and n are the dimensions of the grid, and l is the length of the word being searched for. 
## M: O(mn)

# The coordinates of 'catnip' in the grid are:
# [(1,1)(1,2)(1,3)(2,3)(3,3)(3,4)]