""" /* You have a single collection of data, which contains collections of strings,
 including contestant name, marathon event name, and final position.
 Using this data, write a function that logs a 2-line string for each pair of contestants,
 showing each contestant’s average position amongst all shared events.

####in this example they only have one race against each other, so we just return their positions as it is:
input : [
 ["Billy Blue", "Boston Marathon","76"]
 ["Billy Blue", "New York Marathon", "89"]
 ["Perry Pink", "Boston Marathon", "23"]
 ["Gerald Green", "New York Marathon", "4"]
]

output: "Billy Blue: 76"
"Perry Pink: 23"

"Billy Blue: 89"
"Gerald Green: 4"


##### is this case,  you will notice that contestants might have competed in multiple events with each other. Those positions should be averaged out. The purpose is to find the average finishing position of both contestants in all the events they share with each other. example: Billy Blue and Gerald Green have two marathons in common, the Dallas Marathon and the New York Marathon. Billy Blue finished 89th and 74th in those events, averaging to 81.5, 81 after rounding. Gerald Green finished 4th and 81th in those events, averaging 11th.

data = [
    ["Billy Blue", "Boston Marathon","76"],
    ["Billy Blue", "New York Marathon", "89"],
    ["Perry Pink", "Boston Marathon", "23"],
    ["Billy Blue","Salt Lake City Marathon", "42"],
    ["Perry Pink", "Salt Lake City Marathon", "112"],
    ["Gerald Green", "New York Marathon", "4"],
    ["Gerald Green", "Miami Marathon", "17"],
    ["Rachel Red", "Boston Marathon", "2"],
    ["Gerald Green", "Dallas Marathon", "18"],
    ["Billy Blue", "Dallas Marathon", "74"],
    ["Rachel Red", "New York Marathon", "84"],
]

output:
"Billy Blue: 59"   //// ["Billy Blue", "Boston Marathon","76"], ["Billy Blue","Salt Lake City Marathon", "42"] = 59
"Perry Pink: 67"   //// ["Perry Pink", "Boston Marathon", "23"], ["Perry Pink", "Salt Lake City Marathon", "112"] = 67

"Gerald Green: 11"  /// ["Gerald Green", "New York Marathon", "4"],  ["Gerald Green", "Dallas Marathon", "18"], = 11
"Billy Blue: 81"   //// ["Billy Blue", "New York Marathon", "89"], ["Billy Blue", "Dallas Marathon", "74"] = 81

"Rachel Red: 43"
"Billy Blue: 83"

"Rachel Red: 2"
"Perry Pink: 23"

"Gerald Green: 4"
"Rachel Red: 84" """


from collections import defaultdict


def getPositions(data):

    # runner_info = {}
    # for name, race, position in data:
    #     if name not in runner_info:
    #         runner_info[name] = {}
    #     runner_info[name][race] = int(position)

    # ans = []
    # runners = list(runner_info.keys())
    # for i in range(len(runners)):
    #     for j in range(i+1, len(runners)):
    #         runner1 = runners[i]
    #         runner2 = runners[j]
    #         shared_races = set(runner_info[runner1].keys()).intersection(runner_info[runner2].keys())
    #         if shared_races:
    #             avg1 = sum([runner_info[runner1][race] for race in shared_races]) / len(shared_races)
    #             avg2 = sum([runner_info[runner2][race] for race in shared_races]) / len(shared_races)
    #             avg1, avg2 = int(avg1), int(avg2)
    #             ans.append(f"{runner1}: {avg1}")
    #             ans.append(f"{runner2}: {avg2}")
    # return ans

    runner_info = defaultdict(dict)
    runners = set()

    for name, race, position in data:
        #add all runners into the set
        runners.add(name)
        #create a dict within the dict, with name as key = race : position
        runner_info[name][race] = int(position)
    # print(runners)
    # print(runner_info)


    ans = []
    for r1 in runners:
        for r2 in runners:
            #checking for duplicates. the nested loop will be processed as (r1, r2) and (r2, r1), so we're avoiding both scenarios.
            if r1 >= r2:
                continue

        #find the shared races between 2 runners using 'set && set'
            #get the races from each runner, acessing the runners_info keys at runner name, and making it into a set
            shared_races = set(runner_info[r1].keys() & set(runner_info[r2].keys()))
            #if runners share a race
            if shared_races:

                #get the average from each runner
                #sum of all positions // how many races
                sum1 = 0
                #we're still inside of the for loop, so the shared races only contains the races we care about. so now we can access each runner's position for each race
                for race in shared_races:
                    sum1 += runner_info[r1][race]
                sum2 = 0
                for race in shared_races:
                    sum2 += runner_info[r2][race]    
                
                avg1 = sum1 // len(shared_races)
                avg2 = sum2 // len(shared_races)

                ans.append(f"{r1}, {avg1}, {r2}, {avg2} ******* ")


                # append name and avr in ans
    #return ans
    return ans
            



            

            


""" {
'Billy Blue': {'Boston Marathon': '76', 'New York Marathon': '89', 'Salt Lake City Marathon': '42', 'Dallas Marathon': '74'}, 
'Perry Pink': {'Boston Marathon': '23', 'Salt Lake City Marathon': '112'}, 
'Gerald Green': {'New York Marathon': '4', 'Miami Marathon': '17', 'Dallas Marathon': '18'}, 
'Rachel Red': {'Boston Marathon': '2', 'New York Marathon': '84'}} """


#get the names= 'billy', perry' = 4, 84



data = [
    ["Billy Blue", "Boston Marathon","76"],
    ["Billy Blue", "New York Marathon", "89"],
    ["Perry Pink", "Boston Marathon", "23"],
    ["Billy Blue","Salt Lake City Marathon", "42"],
    ["Perry Pink", "Salt Lake City Marathon", "112"],
    ["Gerald Green", "New York Marathon", "4"],
    ["Gerald Green", "Miami Marathon", "17"],
    ["Rachel Red", "Boston Marathon", "2"],
    ["Gerald Green", "Dallas Marathon", "18"],
    ["Billy Blue", "Dallas Marathon", "74"],
    ["Rachel Red", "New York Marathon", "84"],
]

print(getPositions(data))