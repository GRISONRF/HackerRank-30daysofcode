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
"""
"""


#backtracking

# visited grid = [all cells marked as FALSE]

# HELPER FUNC: check if on bounds /if its a valid cell AND if not visited return true

# DFS -> x, y, char/index of word

    #check if index == len(word) -> means last charac. so we found the word
        # return true
    
    #call helper funct to check if valid coordinate

        #check if grid[x][y] == word[index]
            #if it is: 
            # change coordinates (x,y) from visited grid == True
            # call dfs(x+1, y, index +1) and dfs(x, y+1, index+1)
            #if eihter return true, append the coordinates to coordinates list 


#call - (0,0,0) -> first cell coordinates and fist index of word


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def find_coordinates(grid, word):
   
    rows = len(grid)
    cols = len(grid[0])
    visited_grid = [[False for c in range(cols)] for r in range(rows)]

    
    def is_valid(r, c):
        if r >= 0 and r < rows and c >= 0 and c < cols and visited_grid[r][c] == False:
            return True
        else:
            return False

    def dfs(r, c, i): # row, col, index of word
        # print("dfs({}, {}, {})".format(r, c, i))
        # print(visited_grid)

        #basecase: if i == len(word) -> last word
        if i == len(word):
            return True
        
        if is_valid(r,c):
            #if char in grid same as char in word
            if grid[r][c] == word[i]:
                visited_grid[r][c] = True
                if dfs(r+1, c, i+1):
                    # print(r)
                    # print(c)
                    coordinates.append(tuple([r,c]))
                    return True
                if dfs(r, c+1, i+1):
                    coordinates.append(tuple([r,c]))
                    return True
                    
                visited_grid[r][c] = False

    coordinates = []
    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return coordinates[::-1] # reversing the list to get the correct order
    return None
#----------------------------#


#defines a coordinate class that has two instance variables 'x' and 'y'. and an '__init__' that initializes these variables

#function to find the coordinates. takes the grid and word as arguments
    #m = row, n = col. they are the same size of r and c of original grid
 
    #creates a grid called visited the same size as original grid and mark every cell as FALSE
   

    #func to check if it's a valid coordinate
        #valid if: x is row, so it needs to be greater or equal to 0(starting point in grid) and less than the len of row(end of grid). same for y. AND check if they are NOT visited (if that point in visited is not true)
    


    #start of dfs. takes the x(row), y(col) and index of current char in word being searched for

        #if the index is equal to the len or word, means this is the last char, so we found the word and return True


        # if coordinates are valid and the grid at these coordinates are the same char as the char at word that we're seacrching for, we mark this coordinates in visited as 'TRUE' and set the neighbors [to the right and down the current coordinate]    
  

            #do a DFS in the neighbors
             #check y+1 first, then x+1
                   #if the DFS returns TRUE (means the WORD has been found)
                      #create a Coordinate object using the x and y values and appending to coodinates list. 
                       #return true indicating the word has been found
             # reversing the list to get the correct order
    

grid = [['c', 'c', 'x', 't', 'i', 'b'],
        ['c', 'c', 'a', 't', 'n', 'i'],
        ['a', 'c', 'n', 'n', 't', 't'],
        ['t', 'c', 's', 'i', 'p', 't'],
        ['a', 'o', 'o', 'o', 'a', 'a'],
        ['o', 'a', 'a', 'a', 'o', 'o'],
        ['k', 'a', 'i', 'c', 'k', 'i']]

word = "catnip"
# coordinates = find_coordinates(grid, word)
# if coordinates:
#     print(f"The coordinates of '{word}' in the grid are:")
#     for c in coordinates:
#         print(f"({c.x}, {c.y})")
# else:
#     print(f"'{word}' not found in the grid")



# The coordinates of 'catnip' in the grid are:
# [(1,1)(1,2)(1,3)(2,3)(3,3)(3,4)]


print(find_coordinates(grid, word)) """

#-------------------------------------------------------------------------------------------------------------------------------------

""" The log entry consists of an access time, the ID of the user making the access, and the resource ID. 
The access time is represented as seconds since 00:00:00, and all times are assumed to be within 24 hours.

write a function that takes the logs and returns a data structure that associates to each user their earliest and latest access times.

logs = [
["300", "user_1", "resource5"], ["301", "user_1", "resource3"],["59960", "user_1", "resource3"],]
]
return:
{'user_1': [300, 301]} 


logs1 = [
    ["58523", "user_1", "resource_1"], 
    ["62314", "user_2", "resource_2"], 
    ["54001", "user_1","resource_3"], 
    ["200" , "user_6", "resource_5"], 
    [™215", "user_6", "resource_4"], 
    ["54060", "user_2","resource_3"],
    {53760"user_3", "resource_3"],
    ["58522", "user_22", "resource _1"],
     [™53651", "user_5", "resource_3"],
      ["2", "user_6", "resource_1"], 
      ["100", "user_6", "resource_6"],
      ["488"、"user_7","resource_2"], 
       ["166", "user_8", "resource_6"],
       ["54359"user_1""resource_3"]

user_3:[53760, 53760 ]
user_2: [54060, 62314]

"""


""" def user_access(logs):

    #time, id, resource
    #return user : earliest time, latest time

    # iterate over the logs
    # add into a dict: each user's time

    #access the dict to get the earliest and latest time from each user

    map_user_time = {}

    for time, user, resource in logs:
        time = int(time)

        map_user_time[user] = map_user_time.get(user, []) + [time]

    ans = {}
    for u, t in map_user_time.items():
        time = sorted(t)
        ans[u] = [time[0], time[-1]]
    return ans


# logs = [["300", "user_1", "resource5"], ["301", "user_1", "resource3"],["59960", "user_1", "resource3"]]
# print(user_access(logs))
#{'user_1': [300, 301]}

logs = [["58523", "user_1", "resource_1"], 
    ["62314", "user_2", "resource_2"], 
    ["54001", "user_1","resource_3"],
    ["44001", "user_1","resource_3"], 
    ["200" , "user_6", "resource_5"], 
    ["215", "user_6", "resource_4"], 
    ["54060", "user_2","resource_3"],
    ["53760", "user_3", "resource_3"]]
    


logs1 = [
["58523", "user_1", "resource_1"],
["62314", "user_2", "resource_2"],
["54001", "user_1", "resource_3"],
["200", "user_6", "resource_5"],
["215", "user_6", "resource_4"],
["54060", "user_2", "resource_3"],
["53760", "user_3", "resource_3"],
["58522", "user_22", "resource_1"],
["53651", "user_5", "resource_3"],
["2", "user_6", "resource_1"],
["100", "user_6", "resource_6"],
["400", "user_7", "resource_2"],
["100", "user_8", "resource_6"],
["54359", "user_1", "resource_3"],
]

logs2 = [
["300", "user_1", "resource_3"],
["599", "user_1", "resource_3"],
["900", "user_1", "resource_3"],
["1199", "user_1", "resource_3"],
["1200", "user_1", "resource_3"],
["1201", "user_1", "resource_3"],
["1202", "user_1", "resource_3"]
]

print(user_access(logs1))
# user_3:[53760,53760]
# user_2:[54060,62314]
# user_1:[54001,58523]
# user_7:[400,400]
# user_6:[2,215]
# user_5:[53651,53651]
# user_4:[58522,58522]
# user_8:[100,100] """




""" Write a function that takes the logs and returns the resource with the highest number of accesses in any 5 minute window, together with how many accesses it saw.
Expected Output:
most_requested_resource(logs1) # => ('resource_3', 3)most_requested_resource(logs1) # => ('resource_3', 3)
""" 
"""  
resource and time
return the resource that was accessed the most in 5min (300secs) and how many times in these 5min

map each resource : times

iterate over the map:
    -> max times it was accessed
    -> resource
    
    sliding window with the times. (keep track of how many timestamps in 5min)
    start =0
    end=0
    while start
        while end
            if timestamp[end] - timestamp[start] <= 5min
                keep increasing the end time to get to the 5min (end+=1)
            if more than 5min:
                check if the amount of timestamps > max_times, if it is, update
                and update the resource to curr resource
            start += 1
    
    return max_times and resource
    


"""
""" def most_requested_resource(logs):

#map each resource : times
    map_res_time = {}
    for time, user, log in logs:
        if log not in map_res_time:
            map_res_time[log] = []
        map_res_time[log].append(int(time))
    # print(map_res_time)

#     -> max times it was accessed
    max_timestamp = 0
#     -> resource
    max_resource = None

# iterate over the map:
    for log, times in map_res_time.items():
        times = sorted(times)

    
#     sliding window with the times. (keep track of how many timestamps in 5min - 300s)
#     start =0
        start = 0
    #     end=0
        end= 0
    #     while start
        while start < len(times):
#         while end
            while end < len(times) and times[end] - times[start] <= 300:
#             if timestamp[end] - timestamp[start] <= 5min
                end+=1
#                 keep increasing the end time to get to the 5min (end+=1)
#             if more than 5min:
                if end - start > max_timestamp:
                    max_timestamp = end-start
                    max_resource = log
#                 check if the amount of timestamps > max_times, if it is, update
#                 and update the resource to curr resource
#             start += 1
            start+=1
    
#     return max_times and resource   
    return max_timestamp, max_resource


   
logs1 = [    
    ["58523", "user_1", "resource_1"], 
    ["62314", "user_2", "resource_2"], 
    ["54001", "user_1","resource_3"], 
    ["200" , "user_6", "resource_5"], 
    ["215", "user_6", "resource_4"], 
    ["54060", "user_2","resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"], 
    ["100", "user_6", "resource_6"],
    ["488", "user_7","resource_2"], 
    ["166", "user_8", "resource_6"],
    ["54359", "user_1","resource_3"],
]
print(most_requested_resource(logs1)) # Output: ('resource_3', 3)

logs3 = [    ["300", "user_1", "resource_1"], 
    ["400", "user_2", "resource_2"], 
    ["500", "user_1", "resource_1"], 
    ["600", "user_2", "resource_2"], 
    ["700", "user_1", "resource_1"], 
    ["800", "user_2", "resource_2"], 
    ["900", "user_1", "resource_3"], 
    ["1000", "user_2", "resource_3"], 
    ["1100", "user_1", "resource_3"], 
    ["1200", "user_2", "resource_3"], 
    ["1300", "user_1", "resource_3"], 
    ["1400", "user_2", "resource_3"], 
    ["1500", "user_1", "resource_3"], 
    ["1600", "user_2", "resource_3"], 
    ["1700", "user_1", "resource_4"], 
    ["1800", "user_2", "resource_4"], 
    ["1900", "user_1", "resource_4"], 
    ["2000", "user_2", "resource_4"], 
    ["2100", "user_1", "resource_4"], 
    ["2200", "user_2", "resource_4"], 
    ["2300", "user_1", "resource_4"], 
    ["2400", "user_2", "resource_4"], 
    ["2500", "user_1", "resource_4"], 
    ["2600", "user_2", "resource_4"]
]

# Output: ('resource_3', 4)
print(most_requested_resource(logs3)) # Output: ('resource_3', 6)



logs4 = [    ["58523", "user_1", "resource_1"], 
    ["58524", "user_2", "resource_2"], 
    ["58525", "user_1", "resource_1"],
    ["58526", "user_1", "resource_3"],
    ["58527", "user_2", "resource_3"],
    ["58528", "user_3", "resource_3"],
    ["58529", "user_1", "resource_2"],
    ["58530", "user_3", "resource_2"]
]

print(most_requested_resource(logs4))
# Output: ('resource_3', 3)

# Test Case 3
logs5 = [    ["58523", "user_1", "resource_1"], 
    ["58524", "user_2", "resource_2"], 
    ["58525", "user_1", "resource_1"],
    ["58526", "user_1", "resource_3"],
    ["58527", "user_2", "resource_3"],
    ["58528", "user_3", "resource_3"],
    ["58529", "user_1", "resource_2"],
    ["58530", "user_3", "resource_2"],
    ["58531", "user_3", "resource_3"]
]

print(most_requested_resource(logs5))
 """


#-------------------------------------------------------------------------------------------------------------------------------------


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


""" def flippy(board):


    #index of swipe and how many

    #ans = []  index, how many
    ans = [0,0]

    #iterate over the board
    #we iterate until the len-1 beause since we're comparing to the next element, if we don't do this, we will get an index error
    for i in range(len(board)-1):

        #if X:
        if board[i] == 'X':
            #count = 0
            count = 0

            #while the next char is a O:   i=3    count=3
            while i+1 < len(board)-1 and board[i+1] == 'O':
                print(i+1)
                #add 1 to count
                count+=1
                i+=1
                #keep while going
            #if char == '':
            if board[i+1] == ' ':
                #check if the count > ans[1]
                if count > ans[1]:
                    ans = [i+1, count]
                #if it is, replace ans

        #if "":
        elif board[i] == ' ':
            #count = 0
            count = 0
            #while the next char == 'O':
            while i+1 < len(board)-1 and board[i+1] == 'O':
                #keep while going
                i+=1
                #add 1 to count
                count+=1
            #if char == 'X'
        
            if board[i+1] == 'X':
                #check if count > ans[1]
                if count > ans[1]:
                #if it is, replace ans
                    ans = [i-count, count]

    #return ans
    print(ans)


board = [' ', 'O', 'X'] #0,1
board2 = ['X', 'O', ' ', 'O', 'O', 'O'] #2, 1
board3 = ['X', 'O', 'O', ' ', 'O', 'O', 'O'] #3,2 (if a move captures both left and right we only count the larger of the two captures)
board4 = ['X', 'O', 'X', ' '] #none/null.
print(flippy(board))
print(flippy(board2))
print(flippy(board3))
print(flippy(board4)) """



#-----------------------------------------------------------------------------------------------------------------------------------------



""" There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store.
 You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. 
You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day. """

""" def maxSatisfied(customers, grumpy, minutes):


    #check how many customers are already happy
    already_happy = 0
    #customers and grumpy are the same len, so we can just use the index to access the info of this customer into the grampy array
    for i in range(len(customers)):
        if grumpy[i] == 0:
            already_happy += customers[i]
            #mark the customer as 0 to count these customers as already counted
            customers[i] = 0
    # print(already_happy)


    #use a sliding window to check what is the max number of clients that can be satisfied
    max_happy = 0 # max num of satisfied clients TOTAL
    cur_customers = 0  #keep track of number of satisfied customers in current window

    for i in range(len(customers)):
        
        #add this client to curr customers
        cur_customers += customers[i]

        #check if we are already more or = than X minutes. if so, we want to sutract the first customer to cur_customers [customer [i-minutes]] and update the max_happy with the max value 
        
        if i >= minutes:
            #make the window slide
            cur_customers -= customers[i-minutes]
        max_happy = max(max_happy, cur_customers)

    return max_happy + already_happy


customers = [1,0,1,2,1,1,7,5]
grumpy =    [0,1,0,1,0,1,0,1]
minutes = 3
print(maxSatisfied(customers, grumpy, minutes)) #16

customers = [1, 2, 3, 4, 5]   
grumpy = [0, 1, 0, 1, 0]
x = 2
print(maxSatisfied(customers, grumpy, x)) 
# Expected output: 9


customers = [1, 2, 3, 4, 5]
grumpy = [1, 1, 1, 1, 1]
x = 2
print(maxSatisfied(customers, grumpy, x)) 
# Expected output: 3


customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   #55
grumpy = [1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
x = 3
print(maxSatisfied(customers, grumpy, x)) 
# Expected output: 25


customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
grumpy = [1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
x = 20
print(maxSatisfied(customers, grumpy, x)) 
# # Expected output: 55 """



#-----------------------------------------------------------------------------------------------------------------------------------------



""" You are a developer for a university. Your current project is to develop a system for students to find courses they share with friends. 
The university has a system for querying courses students are enrolled in, returned as a list of (ID, course) pairs.
Write a function that takes in a list of (student ID number, course name) pairs and returns, for every pair of students, a list of all courses they share.
 
Sample Input:
student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]
 
Sample Output (pseudocode, in any order):
 
find_pairs(student_course_pairs_1) =>
{
  [58, 17]: ["Software Design", "Linear Algebra"]
  [58, 94]: ["Economics"]
  [58, 25]: ["Economics"]
  [94, 25]: ["Economics"]
  [17, 94]: []
  [17, 25]: []
} """


""" 
find the shered courses between every student

-> map every course for each student
-> iterate over the map twice to compare one student to another
-> find the intersection between them

"""
""" 
def find_pairs(student_course_pairs):

    map_id_course = {}
    for id, course in student_course_pairs:
        id = int(id)
        if id not in map_id_course:
            map_id_course[id] = set()
        map_id_course[id].add(course)

    ans = {}   #[id, ids] : [c, c, c]

    for s1, c1 in map_id_course.items():
        for s2, c2 in map_id_course.items():
            
            #pay attention to duplicates!!!
            if tuple([s1, s2]) not in ans and tuple([s2, s1]) not in ans and s1 != s2: 

                s_pairs = tuple([s1,s2])

                ans[s_pairs] = c1.intersection(c2)

    res = ""
    for k, v in ans.items():
        res += f'{list(k)}:{list(v)} \n'
    return res



student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]

print(find_pairs(student_course_pairs_1))
"""
'''
Students may decide to take different "tracks" or sequences of courses in the Computer Science curriculum. There may be more than one track that includes the same course, but each student follows a single linear track from a "root" node to a "leaf" node. In the graph below, their path always moves left to right.

Write a function that takes a list of (source, destination) pairs, and returns the name of all of the courses that the students could be taking when they are halfway through their track of courses.

Sample input:
all_courses = [
    ["Logic", "COBOL"],
    ["Data Structures", "Algorithms"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "COBOL"],
    ["Intro to Computer Science", "Data Structures"],
    ["Logic", "Compilers"],
    ["Data Structures", "Logic"],
    ["Creative Writing", "System Administration"],
    ["Databases", "System Administration"],
    ["Creative Writing", "Databases"],
    ["Intro to Computer Science", "Graphics"],
]

Sample output (in any order):
          ["Data Structures", "Creative Writing", "Databases", "Intro to Computer Science"]

All paths through the curriculum (midpoint *highlighted*):

*Intro to C.S.* -> Graphics
Intro to C.S. -> *Data Structures* -> Algorithms -> COBOL
Intro to C.S. -> *Data Structures* -> Logic -> COBOL
Intro to C.S. -> *Data Structures* -> Logic -> Compiler
Creative Writing -> *Databases* -> System Administration
*Creative Writing* -> System Administration
Creative Writing -> *Data Structures* -> Algorithms -> COBOL
Creative Writing -> *Data Structures* -> Logic -> COBOL
Creative Writing -> *Data Structures* -> Logic -> Compilers

Visual representation:

                    ____________
                    |          |
                    | Graphics |
               ---->|__________|
               |                          ______________
____________   |                          |            |
|          |   |    ______________     -->| Algorithms |--\     _____________
| Intro to |   |    |            |    /   |____________|   \    |           |
| C.S.     |---+    | Data       |   /                      >-->| COBOL     |
|__________|    \   | Structures |--+     ______________   /    |___________|
                 >->|____________|   \    |            |  /
____________    /                     \-->| Logic      |-+      _____________
|          |   /    ______________        |____________|  \     |           |
| Creative |  /     |            |                         \--->| Compilers |
| Writing  |-+----->| Databases  |                              |___________|
|__________|  \     |____________|-\     _________________________
               \                    \    |                       |
                \--------------------+-->| System Administration |
                                         |_______________________|

Complexity analysis variables:

n: number of pairs in the input
'''



#-------------------------------------------------------------------------------------------------------------------------------------

""" 
We are working on a security system for a badged-access room in our company's building.
 
Given an ordered list of employees who used their badge to enter or exit the room, write a function that returns two collections:
 
1. All employees who didn't use their badge while exiting the room - they recorded an enter without a matching exit. (All employees are required to leave the room before the log ends.)
 
2. All employees who didn't use their badge while entering the room - they recorded an exit without a matching enter. (The room is empty when the log begins.)
 
Each collection should contain no duplicates, regardless of how many times a given employee matches the criteria for belonging to it.
 
records1 = [
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Martha",   "enter"],
  ["Steve",    "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Paul",     "enter"],
  ["Curtis",   "exit"],
  ["Curtis",   "enter"],
  ["Paul",     "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
  ["Paul",     "enter"],
  ["Paul",     "enter"],
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Paul",     "enter"],
  ["Paul",     "exit"],
  ["Paul",     "exit"]
]
 
Expected output: ["Paul", "Curtis", "Steve"], ["Martha", "Curtis", "Paul"]
 
Other test cases:
 
records2 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
]
 
Expected output: [], []
 
records3 = [
  ["Paul", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
]
 
Expected output: ["Paul"], ["Paul"]
 
records4 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
  ["Paul", "enter"],
]
 
Expected output: ["Paul"], ["Paul"]
 
All Test Cases:
mismatches(records1) => ["Paul", "Curtis", "Steve"], ["Martha", "Curtis", "Paul"]
mismatches(records2) => [], []
mismatches(records3) => ["Paul"], ["Paul"]
mismatches(records4) => ["Paul"], ["Paul"]
 
n: length of the badge records array """
""" def mismatches(records):

    room = set()
    didnt_enter = set()
    didnt_exit = set()

    for p, r in records:
        
        #enter without exiting
        if r == 'enter':
            if p in room:
                didnt_exit.add(p)
            else:
                room.add(p)
        
        if r == 'exit':
            if p not in room:
                didnt_enter.add(p)
            else:
                room.remove(p)
   
    if len(room) != 0:
        for p in room:
            didnt_exit.add(p)
    return list(didnt_exit), list(didnt_enter)

        #exit before entering

    

records1 = [
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Martha",   "enter"],
  ["Steve",    "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Paul",     "enter"],
  ["Curtis",   "exit"],
  ["Curtis",   "enter"],
  ["Paul",     "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
  ["Paul",     "enter"],
  ["Paul",     "enter"],
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Paul",     "enter"],
  ["Paul",     "exit"],
  ["Paul",     "exit"]
]
print(mismatches(records1))

records2 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
]
 
#Expected output: [], []
print(mismatches(records2))

 
records3 = [
  ["Paul", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
]
 
#Expected output: ["Paul"], ["Paul"]
print(mismatches(records3))

 
records4 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
  ["Paul", "enter"],
]
print(mismatches(records4))
#["Paul"], ["Paul"] """



