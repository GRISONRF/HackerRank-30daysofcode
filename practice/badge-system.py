# We are working on a security system for a badged-access room in our company's building.
 
#   Given an ordered list of employees who used their badge to enter or exit the room, write a function that returns two collections:
 
#   1. All employees who didn't use their badge while exiting the room - they recorded an enter without a matching exit. (All employees are required to leave the room before the log ends.)
 
#   2. All employees who didn't use their badge while entering the room - they recorded an exit without a matching enter. (The room is empty when the log begins.)
 
#   Each collection should contain no duplicates, regardless of how many times a given employee matches the criteria for belonging to it.
 
#   records1 = [
#     ["Martha",   "exit"],
#     ["Paul",     "enter"],
#     ["Martha",   "enter"],
#     ["Steve",    "enter"],
#     ["Martha",   "exit"],
#     ["Jennifer", "enter"],
#     ["Paul",     "enter"],
#     ["Curtis",   "exit"],
#     ["Curtis",   "enter"],
#     ["Paul",     "exit"],
#     ["Martha",   "enter"],
#     ["Martha",   "exit"],
#     ["Jennifer", "exit"],
#     ["Paul",     "enter"],
#     ["Paul",     "enter"],
#     ["Martha",   "exit"],
#     ["Paul",     "enter"],
#     ["Paul",     "enter"],
#     ["Paul",     "exit"],
#     ["Paul",     "exit"]
#   ]
 
#   Expected output: ["Paul", "Curtis", "Steve"], ["Martha", "Curtis", "Paul"]
 
#   Other test cases:
 
#   records2 = [
#     ["Paul", "enter"],
#     ["Paul", "exit"],
#   ]
 
#   Expected output: [], []
 
#   records3 = [
#     ["Paul", "enter"],
#     ["Paul", "enter"],
#     ["Paul", "exit"],
#     ["Paul", "exit"],
#   ]
 
#   Expected output: ["Paul"], ["Paul"]
 
#   records4 = [
#     ["Paul", "enter"],
#     ["Paul", "exit"],
#     ["Paul", "exit"],
#     ["Paul", "enter"],
#   ]
 
#   Expected output: ["Paul"], ["Paul"]
 
#   All Test Cases:
#   mismatches(records1) => ["Paul", "Curtis", "Steve"], ["Martha", "Curtis", "Paul"]
#   mismatches(records2) => [], []
#   mismatches(records3) => ["Paul"], ["Paul"]
#   mismatches(records4) => ["Paul"], ["Paul"]
 
#   n: length of the badge records array





from collections import defaultdict


def security_system(records):

    # didnt exit , didn't enter
    room = set()
    no_exit = set()
    no_enter = set()

    for p, record in records:

        if record == "enter":
            if p in room:
                no_exit.add(p)
            else:
                room.add(p)

        elif record == "exit":
            if p not in room:
                no_enter.add(p)
            else:
                room.remove(p)
        
    if room:
        for p in room:
            no_exit.add(p)


    print(f'{list(no_exit)},{list(no_enter)}')

 

#   Expected output: ["Paul", "Curtis", "Steve"], ["Martha", "Curtis", "Paul"]

# print(security_system([
#     ["Martha",   "exit"],
#     ["Paul",     "enter"],
#     ["Martha",   "enter"],
#     ["Steve",    "enter"],
#     ["Martha",   "exit"],
#     ["Jennifer", "enter"],
#     ["Paul",     "enter"],
#     ["Curtis",   "exit"],
#     ["Curtis",   "enter"],
#     ["Paul",     "exit"],
#     ["Martha",   "enter"],
#     ["Martha",   "exit"],
#     ["Jennifer", "exit"],
#     ["Paul",     "enter"],
#     ["Paul",     "enter"],
#     ["Martha",   "exit"],
#     ["Paul",     "enter"],
#     ["Paul",     "enter"],
#     ["Paul",     "exit"],
#     ["Paul",     "exit"]
#   ]))


# print(security_system([
#     ["Paul", "enter"],
#     ["Paul", "enter"],
#     ["Paul", "exit"],
#     ["Paul", "exit"],
#   ])) #   Expected output: ["Paul"], ["Paul"]



# print(security_system([
#     ["Paul", "enter"],
#     ["Paul", "exit"],
#   ]))#   Expected output: [], []




""" SECOND QUESTION

The prompt is asking to create a list of names and the times they swiped their badges, with the condition that the times are within one hour of each other.
If there are multiple intervals that meet this condition, any one of them can be returned.

Input: [['James', '1300'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1530']]
Output: {
'Martha': ['1600', '1620', '1530']
} """


# def oneHour(input):

#     withinOneH = {}
#     personMap = {}
#     for name, time in input:
#         personMap[name] = personMap.get(name, []) + [int(time)]

#     print(personMap)

#     for p, time in personMap.items():
#         for i in range(len(time) -1):
#             if time[i+1] - time[i] <= 100:
#                 if p not in withinOneH:
#                     withinOneH[p] = []
#                 withinOneH[p] += [str(time[i])]
#     print(withinOneH)









# input = [['James', '1300'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1530']]
input = [['James', '1300'], ['Martha', '1700'], ['Martha', '1620'], ['Martha', '1530'], ['Martha', '2530'], ['Martha', '1610'], ['James', '1530']] 

print(oneHour(input))
# Output: { 'Martha': ['1600', '1620', '1530'] }