""" Write a function that takes the logs and returns the resource with the highest number of accesses in any 5 minute window, together with how many accesses it saw.
Expected Output:Expected Output:
most_requested_resource(logs1) # => ('resource_3', 3)most_requested_resource(logs1) # => ('resource_3', 3)

"""


def most_requested_resource(logs):
    # Create a dictionary to store access counts for each resource
    count = {} #resource:[times]
    
    # Iterate through logs and map the times for resources
    for time, user, resource in logs:
        if resource not in count:
            count[resource] = []
        count[resource].append(int(time))
    # print(count)
    
    # Find the resource with the highest access count in any 5-minute window // 600secods
    max_resource = None  #resource that has the highests count in a 5min window
    max_access_count = 0  #access count for that resource


    #iterate over the map
    for resource, time in count.items():
        #sort the time
        time = sorted(time)
        #initialize the start and end of window
        #both start at 0: first loop (where we use the start) represents the index of earliest time and increment it by 1 in each iteration. inner loop increments the 'end' until the difference between the 'start' time and 'end' time is greater than 5 min.

        start = 0
        end = 0

        #outer loop (while start is on bounds of the time)
        while start < len(time):
            #while end is on bounds and end - start not more than 5min
            while end < len(time) and time[end] - time[start] <= 300:
                #if didn't hit the 5min yet, move end to the next time by incrementing its index by 1
                end+=1
            # when the while loop is broken (we hit the 5min) check if the number of timestamps (end - start = the amount of timestamps inside that 5 minutes) is greater than max_count
            if end - start > max_access_count:
                #if it is, substitute max resourse to curr one and the max_count
                max_access_count = end - start
                max_resource = resource
            #also when while loop is broken, update the start in the outer loop    
            start+=1

    #at the end, return both maxs
    return max_access_count, max_resource
   
       
# T: O(mn log m), where m is the number of resources and n is the total number of timestamps.
# M: O(n)


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



logs4 = [    
    ["58523", "user_1", "resource_1"], 
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
