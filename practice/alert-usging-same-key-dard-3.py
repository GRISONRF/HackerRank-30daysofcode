""" LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.

You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and the time when their key-card was used in a single day.

Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".

Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.

Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not considered to be within a one-hour period. """



def alertNames(keyName, keyTime):

    #create a dict to store workername and key time
    workers = {}
    #iterate over both arrays and add them together using zip
    for name, time in zip(keyName, keyTime):
        #check if name already in dict, if not, add to it
        if name not in workers:
            workers[name] = []
        #slip into ":" and convert the string into minutes and add as value for this name
        h, m = map(int, time.split(':'))
        workers[name].append(h * 60 + m)

    #create a list result
    result = []
    #sort names and times
    for name in sorted(workers.keys()):
        times = sorted(workers[name])
        # i and j to keep track of times. initialized as 0 so we check first both cards
        i, j = 0, 0
        
        while j < len(times):
            #if time between time at j and i is within 1h (that's what we're checking)
            if times[j] - times[i] <= 60:
                #increment j by 1
                j += 1
                #check if difference between j and i is >= than 3 (we want to know if keys were used 3+ times)
                if j - i >= 3:
                    #if diff is > than 3, means this worker used the key more than 3 times in 1h. so add name to result
                    result.append(name)
                    #break because we already have their name in the result, dont need to keep checking
                    break
            #if diff between j-i not more than 1h, increment i and loop continues with the next pair of keycard
            else:
                i += 1
    return result


keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
print(alertNames(keyName, keyTime))

keyName1 = ["alice","alice","alice","bob","bob","bob","bob"]
keyTime1 = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
print(alertNames(keyName1, keyTime1))
