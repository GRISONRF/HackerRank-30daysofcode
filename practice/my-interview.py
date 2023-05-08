'''
We have some clickstream data that we gathered on our client's website. We collected snippets of users' anonymized URL histories while they browsed the site. The histories are in chronological order, and no URL was visited more than once per person.

Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.

Sample input:

user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

Sample output:

findContiguousHistory(user0, user1) => ["/pink", "/register", "/orange"]
findContiguousHistory(user0, user2) => [] (empty)
findContiguousHistory(user0, user0) => ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
findContiguousHistory(user2, user1) => ["a"] 
findContiguousHistory(user5, user2) => ["a"]
findContiguousHistory(user3, user4) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user4, user3) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user3, user6) => ["/tan", "/red", "/amber"]
findContiguousHistory(user6, user3) => ["/tan", "/red", "/amber"]

n: length of the first user's browsing history
m: length of the second user's browsing history
'''

user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

# Note: built-in functions like the Python difflib module should not be used as solutions to this problem

def findContiguousHistory(user1, user2):
    
     #user1 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
     #user2 = ["/start", "/pink", "/register", "/orange", "/red", "a"]


    # result = []
    # max_len = 0

    # for i in range(len(user1)):
    #     for j in range(len(user2)):

    #         records = []
            
    #         k = 0
    #         while (i+k < len(user1)) and (j+k < len(user2)) and user1[i+k] == user2[j+k]:
    #             # print(user1[i+k])
    #             records.append(user1[i+k]) 
    #             k +=1
            
    #         if len(records) > max_len:
    #             # print(records)
    #             result.append(records)
    #             max_len = len(records)
                
    # # return result
    # # print(result)


    result = []
    
    #iterate over user0
    for i1 in range(len(user1)): # i1 =0
        
        #creating list to temp max
        
        #iterate over user1
        for i2 in range(len(user2)): #i2 = 0
            # print(user1[i1])
            maybe_max = []
            
            #check if str1 == str2
            if user1[i1] == user2[i2]:   
                #if they're the same, add to maybe_max and start checking the next strings
                    #while str1+1 == str2+1 and on bounds
                j = 0
                while i2 + j < len(user2) and i1 + j < len(user1) and user1[i1 + j] == user2[i2 + j]: 
                    #add to maybe max\
                    maybe_max.append(user1[i1 + j])
                    #increment j+1
                    j +=1

                #update max_len
                if len(maybe_max) > len(result):
                    result = maybe_max
    print(result)


#T: O(N^3) ->because it has two nested loops that iterate over both users, and then there is another while loop that has a worst-case scenario of iterating over both users again, making it cubic time complexity.
#M: O(N)

print(findContiguousHistory(user3, user4))
findContiguousHistory(user0, user1) # ["/pink", "/register", "/orange"]
findContiguousHistory(user0, user2) # [] (empty)
findContiguousHistory(user0, user0) # ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
findContiguousHistory(user2, user1) # ["a"] 
findContiguousHistory(user5, user2) # ["a"]
findContiguousHistory(user3, user4) # ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user4, user3) # ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user3, user6) # ["/tan", "/red", "/amber"]
findContiguousHistory(user6, user3) # ["/tan", "/red", "/amber"]

    # #create a set with user 1
    # set1 = set(user2)

    # #store the max total / result
    # max_l = []

    # #iterate over user2
    # for i in range(len(user2)):

    #     potencial_max = []
    #     #if cur string is present in other user list
    #     if user2[i] in set1:

    #         # add it to potential max
    #         potencial_max.append(user2[i])

    #         #sliding window kinda of? -> i want to iterate over both 
    #         j=0
    #         for j in range(len(i+j, len(user2))):
    #             if user2[i+j] == user2[]








    # max_len = []
    
    # #iterate over user1
    # for i1 in range(len(user1) -1): # i1 =0
        
    #     #creating list to temp max
    #     maybe_max = []
        
    #     #iterate over user2
    #     for i2 in range(len(user2)): #i2 = 0
    #         # print(user1[i1])
            
    #         #check if str1 == str2
    #         if user1[i1] == user2[i2]:   
    #             #if they're the same, add to maybe_max
    #                 #while str1+1 == str2+1
    #                 j = 0
    #                 while i2 + j < len(user2) and i1 + j < len(user1) and user1[i1 + j] == user2[i2 + j]: 
    #                     #add to maybe max\
    #                     maybe_max.append(user1[i2 + j])
    #                     #increment j+1
    #                     j +=1
    #                 #update max_len
    #                 max_len = max(max_len, maybe_max)
    #     print(maybe_max)
                
                   
                
        
        #max_len = max(max_len, mmaybe)
    
    
    
   


# print(findContiguousHistory(user0, user1))














#create a map with domain as key and count as the value
    # iterate over the list
        #split "," count, domain = ['google', 'com']
        #
        
from collections import defaultdict
        
def calculateClicksByDomain(counts):
    
    domain_count_map = defaultdict(int)
    
    for domain in counts:
        count, domain = domain.split(',')
        
        count = int(count)
        subdomain = domain.split('.')
        
        for i in range(len(subdomain)):


            domain_count_map[".".join(subdomain[i:])] += count
        
    return domain_count_map


counts = [
    "900,google.com",
    "60,mail.yahoo.com",
    "10,mobile.sports.yahoo.com",
    "40,sports.yahoo.com",
    "300,yahoo.com",
    "10,stackoverflow.com",
    "20,overflow.com",
    "5,com.com",
    "2,en.wikipedia.org",
    "1,m.wikipedia.org",
    "1,mobile.sports",
    "1,google.co.uk" 
]


# print(calculateClicksByDomain(counts))






'''
For a new autocorrect system, we want to find the relationships between frequently typed in words and similar words that are one letter longer.

Given two strings s1 and s2, we will call (s1, s2) a "step" if you can form s2 by adding exactly one letter to s1 and possibly rearranging the letters of s1.

For example:
(OF, FOR) is a step
(OF, IF) is not a step
(OF, OCT) is not a step
(ERA, EAR) is not a step
(SHE, SHEEP) is not a step
(TEE, TEST) is not a step

Given a wordlist, produce an index of possible one-letter steps
   w -> {  w1 | (w, w1) is a step } 
that associates to each word all the words in the wordlist that are a step away from it.

wordlist = [
  ["OF",   "30966074"],
  ["FOR",   "6545282"],
  ["NO",    "6545282"],
  ["ON",    "4594521"],
  ["NOT",   "4522732"],
  ["FROM",  "3469207"],
  ["ONE",   "2148983"],
  ["INTO",  "1144226"],
  ["OUGHT",  "785433"],
  ["THOUGH", "785433"],
  ["SOUGHT", "785433"],
  ["THOUGHT","785433"],
  ["NOW",    "679337"],
  ["FOUR",   "679337"],
  ["FORM",   "352032"],
  ["OFF",    "333858"],
  ["POINT",  "333858"],
  ["LEFT",   "306802"],
  ["FORMS",  "136468"]
]

one_letter_steps_index = step_index(wordlist)

# Expected output (pseudocode, unordered):

NO     : [ ONE, NOT, NOW ]
INTO   : [ POINT ]
LEFT   : []
FORM   : [ FORMS ]
ONE    : []
FOUR   : []
FOR    : [ FORM, FOUR, FROM ]
FROM   : [ FORMS ]
OFF    : []
OUGHT  : [ THOUGH, SOUGHT ]
SOUGHT : []
THOUGH : [ THOUGHT ]
THOUGHT: []
FORMS  : []
NOT    : [ INTO ]
OF     : [ FOR, OFF ]
NOW    : []
POINT  : []
ON     : [ ONE, NOT, NOW ]

Complexity analysis variables:  
  
N = The number of words  
L = The length of words  
'''

wordlist = [
    ["OF", "30966074"],
    ["FOR", "6545282"],
    ["NO", "6545282"],
    ["ON", "4594521"],
    ["NOT", "4522732"],
    ["FROM", "3469207"],
    ["ONE", "2148983"],
    ["INTO", "1144226"],
    ["OUGHT", "785433"],
    ["THOUGH", "785433"],
    ["SOUGHT", "785433"],
    ["THOUGHT", "785433"],
    ["NOW", "679337"],
    ["FOUR", "679337"],
    ["FORM", "352032"],
    ["OFF", "333858"],
    ["POINT", "333858"],
    ["LEFT", "306802"],
    ["FORMS", "136468"],
]

def step_index(wordlist):

    result = {}
    #iterates over wordlist
    for i in range(len(wordlist)):
        #word 1
        w1 = wordlist[i][0]
        #add this word as a key to the result with an empty list as value
        result[w1] = []

        #iterate over the word list again
        for j in range(len(wordlist)):
            #if the indexes are the same, ignore
            if i == j:
                continue
            #sava the word into w2
            w2 = wordlist[j][0]

            #if len of both words dont have a 1 diff, ignore
            if len(w2) - len(w1) != 1:
                continue

            #create lists using the words
            w1_chars = list(w1)
            w2_chars = list(w2)
            #check if letters match
            for c in w1_chars:
                if c in w2_chars:
                    w2_chars.remove(c)
                else:
                    break
            #if for loop ran without encountering the break. means this is a valid result
            else:
                result[w1].append(w2)
    
    return result
    
    
    
    
# print(step_index(wordlist))



# counts = word, frquency
# create a dictionary to map word and freq -> only add the ones that matches len from 2 to X
# sort the items in dict by the frequency



def top(counts, need_words, max_word_length):
    
    map_word_freq = {}
    for item in counts:
        word, count = item.split(',')
        if len(word) >= 2 and len(word) <= max_word_length:
            if word not in map_word_freq:
                map_word_freq[word] = int(count)
     
    sorted_map = sorted(map_word_freq.items(), key=lambda item:item[1], reverse=True)   
    
    ans = []
    count = 0
    for w, f in sorted_map:
        count += 1
        if count <= need_words:
            ans.append(([w, f]))
    return ans
    
    



# print(top(counts1, need_words = 12, max_word_length = 5))
# print(top(counts2, need_words = 1, max_word_length = 3))
# print(top(counts2, need_words = 3, max_word_length = 3))

# Test case 1
# counts1 = ['apple,5', 'banana,3', 'cherry,2', 'durian,7', 'eggplant,1', 'fig,5']
# result1 = top(counts1, need_words=3, max_word_length=6)
# print(result1)
# # Expected output: [('durian', 7), ('apple', 5), ('fig', 5)]

# # Test case 2
# counts2 = ['a,10', 'at,3', 'cat,7', 'rat,5', 'dog,2', 'car,1', 'cab,2', 'act,5']
# result2 = top(counts2, need_words=2, max_word_length=3)
# print(result2)
# # Expected output: [('cat', 7), ('rat', 5)]

# # Test case 3
# counts3 = ['one,4', 'two,3', 'three,2', 'four,1']
# result3 = top(counts3, need_words=4, max_word_length=4)
# print(result3)
# # Expected output: [('one', 4), ('two', 3), ('three', 2), ('four', 1)]


"""
You are working on a logic game made up of a series of puzzles. The first type of puzzle you settle on is "sub-Sudoku", a game where the player has to position the numbers 1..N on an NxN matrix.

Your job is to write a function that, given an NxN matrix, returns true if  every row and column contains the numbers 1..N

The UI for the game does not do any validation on the numbers the player enters, so the matrix can contain any signed integer.

grid1 = [[2, 3, 1],
         [1, 2, 3],
         [3, 1, 2]]            -> True

grid2 = [[1, 2, 3],
         [3, 2, 1],
         [3, 1, 2]]            -> False

grid3 = [[2, 2, 3],
         [3, 1, 2],
         [2, 3, 1]]            -> False

grid4 = [[1]]                  -> True

grid5 = [[-1, -2, -3],
         [-2, -3, -1],
         [-3, -1, -2]]         -> False

grid6 = [[1, 3, 3],
         [3, 1, 2],
         [2, 3, 1]]            -> False

grid7 = [[1, 2, 3, 4],
         [4, 3, 2, 1],
         [1, 3, 2, 4],
         [4, 2, 3, 1]]         -> False

grid8 = [[0, 3],
         [3, 0]]               -> False

grid9 = [[0, 1],
         [1, 0]]               -> False

grid10 = [[0, 2],
          [2, 0]]              -> False

grid11 = [[1, 2, 3, 4],
          [2, 3, 1, 4],
          [3, 1, 2, 4],
          [4, 2, 3, 1]]        -> False

grid12 = [[-1, -2, 12, 1],
          [12, -1, 1, -2],
          [-2, 1, -1, 12],
          [1, 12, -2, -1]]     -> False

grid13 = [[2, 3, 3],
          [1, 2, 1],
          [3, 1, 2]]           -> False

grid14 = [[1, 3],              -> False
          [3, 1]]

grid15 = [[2, 3],              -> False
          [3, 2]]

grid16 = [[3, 2],              -> False
          [2, 3]]

validateSudoku(grid1) => True
validateSudoku(grid2) => False
validateSudoku(grid3) => False
validateSudoku(grid4) => True
validateSudoku(grid5) => False
validateSudoku(grid6) => False
validateSudoku(grid7) => False
validateSudoku(grid8) => False
validateSudoku(grid9) => False
validateSudoku(grid10) => False
validateSudoku(grid11) => False
validateSudoku(grid12) => False
validateSudoku(grid13) => False
validateSudoku(grid14) => False
validateSudoku(grid15) => False
validateSudoku(grid16) => False
  
Complexity analysis variables:  
  
N = The number of rows/columns in the matrix  
"""

# number in the grid 1 - n


def validateSudoku(grid):
    
    # numbers in the row and col if numbers are from 1 to n
    # n = size of col 
    #iterate grid
    # n = len(grid)  # (1, 2, ...n)
    
    # for r in range(len(grid)):     
    #     for c in range(len(grid[0])):
    #         num_row = []
    #         if grid[r][c] in num_row:
                
    nums = []
    for i in range(1, len(grid)+1):
        nums.append(i)
        
    cols = [row[0] for row in grid]
        
        
    for r in range(len(grid)):     
        for c in range(len(grid[0])):
            
                        
            for n in nums:
            
                #rows
                if n not in grid[r]:
                    return False
                
                # print([row[c] for row in grid])
                
                if n not in [row[r] for row in grid]:
                    return False
                
                else:
                    return True
                #print(n)
                #print([row[r] for row in grid])
       
    return True
             
        
    
    
    

grid1 = [
    [2, 3, 1],
    [1, 2, 3],
    [3, 1, 2],
]


grid2 = [
    [1, 2, 3],
    [3, 2, 1],
    [3, 1, 2],
]

grid3 = [
    [2, 1, 3],
    [3, 1, 2],
    [2, 3, 1],
]

grid4 = [
    [1],
]
grid5 = [
    [-1, -2, -3],
    [-2, -3, -1],
    [-3, -1, -2],
]
grid6 = [
    [1, 3, 3],
    [3, 1, 2],
    [2, 3, 1],
]
grid7 = [
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [1, 3, 2, 4],
    [4, 2, 3, 1],
]
grid8 = [
    [0, 3],
    [3, 0],
]
grid9 = [
    [0, 1],
    [1, 0],
]
grid10 = [
    [0, 2],
    [2, 0],
]
grid11 = [
    [1, 2, 3, 4],
    [2, 3, 1, 4],
    [3, 1, 2, 4],
    [4, 2, 3, 1],
]
grid12 = [
    [-1, -2, 12, 1],
    [12, -1, 1, -2],
    [-2, 1, -1, 12],
    [1, 12, -2, -1],
]
grid13 = [
    [2, 3, 3],
    [1, 2, 1],
    [3, 1, 2],
]
grid14 = [
    [1, 3],
    [3, 1],
]
grid15 = [
    [2, 3],
    [3, 2],
]
grid16 = [
    [3, 2],
    [2, 3],
]

print(validateSudoku(grid1))# => True
print(validateSudoku(grid2))# => False
print(validateSudoku(grid3))# => False
print(validateSudoku(grid4))# => True
print(validateSudoku(grid5))# => False
print(validateSudoku(grid6))# => False
print(validateSudoku(grid7))# => False
print(validateSudoku(grid8))# => False
print(validateSudoku(grid9))# => False
print(validateSudoku(grid10))# => False
print(validateSudoku(grid11))# => False
print(validateSudoku(grid12))# => False
print(validateSudoku(grid13))# => False
print(validateSudoku(grid14))# => False
print(validateSudoku(grid15))# => False
print(validateSudoku(grid16))# => False





'''
You are working on an accounting program for an event's ticketing system.

At the end of the day, all the payments received from the payment gateway have to be matched with the users who bought the tickets. There is always a 1-to-1 match between the users and the payments.

Write a function that, given the payment, pricing, and user data, returns a data structure that links the names of the users to their payment IDs, based on the rules described below.

First, orders can be match by the users' emails. If the emails don't match, use the payment amounts. For each payment amount, there will be at most one payment that cannot be matched via the email.

For this problem, we can assume the names are unique.

Users:
---------------------------------------------------------
| Name        | Email            | Purchase  | Quantity |
---------------------------------------------------------
| John A.     |  john.a@mail.com | Top       |        3 |
| James S.    |     j.s@mail.com | Economy   |        2 |
| Stacy C.    | stacy.c@test.com | Economy   |        2 |
| Bobby B.    |     bob@mail.com | Medium    |       10 |
| Michelle X. |     mix@test.com | Medium    |       10 |
| Linda F.    |     l.f@mail.com | Top       |       10 |
| Betty T.    |     b.t@mail.com | ThreeEco  |        1 |
| Nancy L.    |     n.l@test.com | TwoEco    |        1 |
| Daniel O.   |     d.o@mail.com | OneEco    |        1 |
| Mike E.     |     m.e@mail.com | FourEco   |        1 |
| Matthew R.  |      mr@test.com | OneEco    |        5 |
| Albert K.   |  albert@test.com | OneEco    |        5 |
---------------------------------------------------------

Payment Gateway:
-----------------------------------
| ID | Email             | Amount |
-----------------------------------
|  1 |    john2@mail.com |     33 |
|  2 | michelle@mail.com |     60 |
|  3 |  stacy.c@test.com |      8 |
|  4 |    james@mail.com |      8 |
|  5 |      bob@mail.com |     60 |
|  6 |   email not found |    110 |
|  7 |   email not found |      1 |
|  8 |   email not found |      2 |
|  9 |   email not found |      3 |
| 99 |   email not found |      4 |
| 10 |       mr@test.com |      5 |
| 11 |        a@mail.com |      5 |
-----------------------------------

Ticket Prices:
--------------------
| Ticket   | Price |
--------------------
| Economy  |     4 |
| Top      |    11 |
| Medium   |     6 |
| OneEco   |     1 |
| TwoEco   |     2 |
| ThreeEco |     3 |
| FourEco  |     4 |
--------------------

Expected results


matching(users,payments,prices) =>
# Payment ID -> Name
5  -> Bobby B.     # Bobby's email (bob@mail.com) matches
3  -> Stacy C.     # Stacy's email (stacy.c@test.com) matches
10 -> Matthew R.   # Matthew's email (mr@test.com) matches
6  -> Linda F.     # The amount matches, 10 Top tickets at 11
7  -> Daniel O.    # The amount matches, 1 OneEco ticket at 1
8  -> Nancy L.     # The amount matches, 1 TwoEco ticket at 2
9  -> Betty T.     # The amount matches, 1 ThreeEco ticket at 3
99 -> Mike E.      # The amount matches, 1 FourEco ticket at 4
1  -> John A.      # John's amount matches, being the only payment for 33 with 3 Top tickets at 11
2  -> Michelle X.  # It's the only payment for 60 without a matching email
4  -> James S.     # James because it's the only other payment for 8
11 -> Albert K.    # It's the only other payment for 5 without a matching email


Complexity variables:

U = number of users or payments
T = number ticket prices
'''
#ans = []

# iterate ppayments
# map_email =  email: [id] [amount]  //when "email not found", i would create a new dict: {email not found = id:amount}

#iterate useres
 #check if email is in map_email
    #if it is, know for sure so add ro as [email, name, true]

    #if email is not:
        #check inside of email_not_found dictionary:
            # check on purchase and multiply the price * quantity
                #look for price * quantity in map_email_not_found][1]
                
        
















# 1. It has to be at least 16 characters long.
# 2. The password cannot contain the word "password". This rule is not case-sensitive.
# 3. The same character cannot be used more than 4 times. This rule is case-sensitive, "a" and "A" are different characters.
# 4. The password has to contain at least one uppercase and one lowercase letter.
# 5. The password has to contain at least one of the following special characters "*","#","@".

# ans = []
# iterate string
    # if its not 16 long, add 1 to the []
    
 # NOT MET   
def validate(password):
    
    ans = []
        
    if len(password) < 16:
        ans.append([1])
        
    # print(password.lower())
    if 'password' in password.lower():
        ans.append([2])
    
    repeated_l = {}
    for s in password:
        
        if s in repeated_l:
            repeated_l[s] += 1
        else:
            repeated_l[s] = 1
    
    for char, count in repeated_l.items():
        if count > 4:
            ans.append([3])
            break
            
    check_up = False 
    check_l = False        
    for s in password:
        if s.isupper():
            check_up = True
        if s.islower():
            check_l = True
    if check_l == False or check_up == False:
        ans.append([4])
                    
        
    special_char = False
    for char, count in repeated_l.items():
        if char in ["*","#","@"]:
            special_char = True
    if special_char == False:
        ans.append([5])

    return ans
            
    




# password_1 = "Strongpwd9999#abc"
# password_2 = "Less10#"
# password_3 = "Password@"
# password_4 = "#PassWord011111112222223x"
# password_5 = "password#1111111"
# password_6 = "aaaapassword$$"
# password_7 = "LESS10#"
# password_8 = "SsSSSt#passWord"

print(validate(password_3))
print(validate(password_1)) # []
print(validate(password_2)) # [1]
print(validate(password_3)) # [1,2]
print(validate(password_4)) # [2,3]
print(validate(password_5)) # [2,3,4]
print(validate(password_6)) # [1,2,3,4,5]
print(validate(password_7)) # [1,4]
print(validate(password_8)) # [1,2]

users = [
	["John A.", "john.a@mail.com", "Top", "3"],
	["James S.", "j.s@mail.com", "Economy", "2"],
	["Stacy C.", "stacy.c@test.com", "Economy", "2"],
	["Bobby B.", "bob@mail.com", "Medium", "10"],
	["Michelle X.", "mix@test.com", "Medium", "10"],
	["Linda F.", "l.f@mail.com", "Top", "10"],
	["Betty T.", "b.t@mail.com", "ThreeEco", "1"],
	["Nancy L.", "n.l@test.com", "TwoEco", "1"],
	["Daniel O.", "d.o@mail.com", "OneEco", "1"],
	["Mike E.", "m.e@mail.com", "FourEco", "1"],
	["Matthew R.", "mr@test.com", "OneEco", "5"],
	["Albert K.", "albert@test.com", "OneEco", "5"]
]

payments = [
	["1", "john2@mail.com", "33"],
	["2", "michelle@mail.com", "60"],
	["3", "stacy.c@test.com", "8"],
	["4", "james@mail.com", "8"],
	["5", "bob@mail.com", "60"],
	["6", "email not found", "110"],
	["7", "email not found", "1"],
	["8", "email not found", "2"],
	["9", "email not found", "3"],
	["99", "email not found", "4"],
	["10", "mr@test.com", "5"],
	["11", "a@mail.com", "5"]
]

prices = [
	["Economy", "4"],
	["Top", "11"],
	["Medium", "6"],
	["OneEco", "1"],
	["TwoEco", "2"],
	["ThreeEco", "3"],
	["FourEco", "4"]
]
