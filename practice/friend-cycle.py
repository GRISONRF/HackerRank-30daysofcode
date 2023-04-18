""" Given employees and friendships, find all adjacencies that denote the friendship, 
A friendship is bi-directional/mutual so if 1 is friends with 2, 2 is also friends with 1.

Sample Input:
employees = [
  "1, Bill, Engineer",
  "2, Joe, HR",
  "3, Sally, Engineer",
  "4, Richard, Business",
  "6, Tom, Engineer"
]

friendships = [
  "1, 2",
  "1, 3",
  "3, 4"
]

Sample Output:
Output: LIST OF STRINGS
"1: 2, 3
2: 1
3: 1, 4
4: 3
6: None" """


""" 
employee_dict = {}
iterate over employee
    split items of employee at the ", "
    add to the dict the employee id as the key and the value as a set()

iterate over friendships: 
    split the friends at the ", "
   add each friend at each other's name in the dictionary

ans = []
for employee and friend in the employee dict
    if this employee has a friend
        friend_str = create a string out of friend in set. we want to join them with a ", "
    if this employee has no friend
        friend_str = None
    at the end add the friend_str in the ans
return ans


"""
    

def friend_cycle(employees, friendships):

    friend_map = {}
    for e in employees:
        id, name, role = e.split(', ')
        friend_map[id] = set()
    
    for f in friendships:
        f1, f2 = f.split(', ')

        friend_map[f1].add(f2)
        friend_map[f2].add(f1)

    ans = []
    for e, f in friend_map.items():
        if f:
            f_str = ", ".join(f)
        else:
            f_str = None
        ans.append(f'{e}: {f_str}')

    print(ans)

    

        






employees = [
  "1, Bill, Engineer",
  "2, Joe, HR",
  "3, Sally, Engineer",
  "4, Richard, Business",
  "6, Tom, Engineer"
]

friendships = [
  "1, 2",
  "1, 3",
  "3, 4"
]
print(friend_cycle(employees, friendships))

# def friend_cycle(employees, friendships):

#     employee_dict = {}
#     for e in employees:
#         id, name, role = e.split(', ') #remember of space after comma
#         employee_dict[id] = set()

#     for f in friendships:
#         f1, f2 = f.split(', ') #remember of space after comma
#         employee_dict[f1].add(f2)
#         employee_dict[f2].add(f1)
    
#     ans = []
#     for e, f in employee_dict.items():

#         if f:
#             f_str = ", ".join(f)
#         else:
#            f_str = None
#         ans.append(f'{e}: {f_str}')

#     print(ans)