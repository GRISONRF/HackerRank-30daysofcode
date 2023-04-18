'''
You are reading a Build Your Own Story book. It is like a normal book except that choices on some pages affect the story, sending you to one of two options for your next page.

You start reading at page 1 and read forward one page at a time unless you reach a choice or an ending.

The choices are provided in a list, sorted by the page containing the choice, and each choice has two options of pages to go to next. In this example, you are on page 3, where there is a choice. Option 1 goes to page 7 and Option 2 goes to page 8.

choices1_1 = [[3, 7, 8], [9, 4, 2]] => [[current_page, option_1, option_2], ...]
The ending pages are also given in a sorted list:

endings1 = [6, 15, 21, 30]

These choices are really stressing you out, so you decide that you'll either always pick the first option, or always pick the second option.

Given a list of endings, a list of choices with their options, and the choice you will always take (Option 1 or Option 2), return the ending you will reach. If you get stuck in a loop, return -1.

Example:
find_ending(endings1, choices1_1, 1) (always Option 1)
  Start: 1 -> 2 -> 3(choice) -> 7 -> 8 -> 9(choice) -> 4 -> 5 -> 6(end) => Return 6

find_ending(endings1, choices1_1, 2) (always Option 2)
  Start: 1 -> 2 -> 3(choice) -> 8 -> 9(choice) -> 2 -> 3(choice) -> 8 ... => Return -1

Additional inputs:
choices1_2 = [[3, 14, 2]]
choices1_3 = [[5, 11, 28], [9, 19, 29], [14, 16, 20], [18, 7, 22], [25, 6, 30]]
choices1_4 = [[2, 10, 15], [3, 4, 10], [4, 3, 15], [10, 3, 15]]

endings2 = [11]
choices2_1 = [[2, 3, 4], [5, 10, 2]]
choices2_2 = []

Complexity Variable:
n = number of pages
(endings and choices are bound by the number of pages)

All Test Cases :
stories(endings1, choices1_1, 1) => 6
stories(endings1, choices1_1, 2) => -1
stories(endings1, choices1_2, 1) => 15
stories(endings1, choices1_2, 2) => -1
stories(endings1, choices1_3, 1) => 21
stories(endings1, choices1_3, 2) => 30
stories(endings1, choices1_4, 1) => -1
stories(endings1, choices1_4, 2) => 15
stories(endings2, choices2_1, 1) => 11
stories(endings2, choices2_1, 2) => -1
stories(endings2, choices2_2, 1) => 11
stories(endings2, choices2_2, 2) => 11
'''

endings1 = [6, 15, 21, 30]
choices1_1 = [
    [3, 7, 8],
    [9, 4, 2],
]
choices1_2 = [
    [3, 14, 2],
]
choices1_3 = [
    [5, 11, 28],
    [9, 19, 29],
    [14, 16, 20],
    [18, 7, 22],
    [25, 6, 30],
]
choices1_4 = [
    [2, 10, 15],
    [3, 4, 10],
    [4, 3, 15],
    [10, 3, 15],
]

endings2 = [11]
choices2_1 = [
    [2, 3, 4],
    [5, 10, 2],
]
choices2_2 = []


# find_ending(endings1, choices1_1, 1) (always Option 1)
#   Start: 1 -> 2 -> 3(choice) -> 7 -> 8 -> 9(choice) -> 4 -> 5 -> 6(end) => Return 6

# choices1_1 = [[3, 7, 8], [9, 4, 2]]
# endings1 = [6, 15, 21, 30]

def find_ending(endings, choices, option):
    # create a dictionary to store the mapping from current page to the next page
    cmap = {}
    # loop through the `choices` list
    for c in choices:
        # store the current page as key, and next page as value in the `cmap` dictionary
        # the value is either `c[1]` (index 1) if `option` is 1, or `c[2]` (index 2) if `option` is 2
        cmap[c[0]] = c[1] if option == 1 else c[2]
    # create a set to store the pages that have been visited
    seen = set()
    # initialize the starting page number as `i`
    i = 1
    # continue the loop until the maximum ending page is reached
    while i <= endings[-1]:
        # check if the current page `i` is one of the endings
        if i in endings:
            # return `i` if it is one of the endings
            return i
        # add the current page `i` to the `seen` set
        seen.add(i)
        # check if the `cmap` dictionary contains the current page `i`
        if i in cmap:
            # update the next page `i` with the value from `cmap`
            i = cmap[i]
            # check if the next page `i` has already been visited
            if i in seen:
                # return -1 if there is a loop
                return -1
        else:
            # increment `i` if the current page `i` is not in `cmap`
            i += 1
    # return -1 if no ending is found
    return -1
        
    
print(find_ending(endings1, choices1_1, 1))
print(find_ending(endings1, choices1_1, 2))# -1
print(find_ending(endings1, choices1_2, 1))# 15
print(find_ending(endings1, choices1_2, 2))# -1
print(find_ending(endings1, choices1_3, 1))# 21
print(find_ending(endings1, choices1_3, 2))# 30
print(find_ending(endings1, choices1_4, 1))# -1
print(find_ending(endings1, choices1_4, 2))# 15
print(find_ending(endings2, choices2_1, 1))# 11
print(find_ending(endings2, choices2_1, 2))# -1
print(find_ending(endings2, choices2_2, 1))# 11
print(find_ending(endings2, choices2_2, 2))# 11