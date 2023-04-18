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

def user_access(logs):

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

logs2 = [["58523", "user_1", "resource_1"], 
    ["62314", "user_2", "resource_2"], 
    ["54001", "user_1","resource_3"], 
    ["200" , "user_6", "resource_5"], 
    ["215", "user_6", "resource_4"], 
    ["54060", "user_2","resource_3"],
    ["53760", "user_3", "resource_3"]]
    
print(user_access(logs2))
