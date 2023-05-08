""" Write a function that takes the logs and returns the resource with the highest number of accesses in any 5 minute window, together with how many accesses it saw.
Expected Output:Expected Output:
most_requested_resource(logs1) # => ('resource_3', 3)most_requested_resource(logs1) # => ('resource_3', 3)

"""


def most_requested_resource(logs):
    
  #highest number of access in 5 min
  #300 seconds
  
  #resource: [times]
  res_map = {}
  for time, user, res in logs:
    if res not in res_map:
      res_map[res] = list()
    res_map[res].append(int(time))

  max_res = None
  max_count = 0

  for res, time in res_map.items():
    time = sorted(time)
    
    start = 0
    end = 0 #1
    while start < len(time):
      
      while end < len(time) and time[end] - time[start] <= 300:
        end +=1
      
      if end != start:

        curr_count = end - start

        if curr_count > max_count:
          max_count = curr_count
          max_res = res
      
      start +=1
      end = start

  print(max_res, max_count)

#T: O(n^2) -> sorted is only sorting though times which is smaller than the logs
#M: O(n)
    

    







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
print(most_requested_resource(logs3)) 



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
