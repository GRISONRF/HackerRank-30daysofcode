""" Given a list of [name, time], where the time is in string format: '1300' // 1 PM in the afternoon.

return: list of names and the times where their swipe badges within one hour. if there are multiple intervals that satisfy the condition, return any one of them.
name1: time1, time2, time3...
name2: time1, time2, time3, time4, time5...
example:
input: [['James', '1300'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1530']] 
output: {
'Martha': ['1600', '1620', '1530']
}

"""
""" 
create a dict to map each person to the times they used the badge
    - convert time to string

ans = []
iterate over the map
    -sort the time
    times_interval = []
    -iterate over the times
        -check if times have a 1h difference between them
        -if they have an 1h interval, add the times in the times_interval list
    add times_interval to ans
return ans

"""
def frequentAccess(records):

    map_p_t = {}
    for p, t in records:
        if p not in map_p_t:
            map_p_t[p] = []
        map_p_t[p].append(int(t))
    
    ans = []
    for name, times in map_p_t.items():
        s_times = sorted(times)

        intervals = []
        start = 0
        end = 0

        while end < len(times) and s_times[end] - s_times[start] <= 100:
            end += 1
        if end - start > 1:
            intervals.append(s_times[start:end])
        start += 1

        if intervals:
            ans.append((name, intervals[-1]))

    return ans





records = [['James', '1300'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1530']] 
print(frequentAccess(records))


records2 = [['James', '1300'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1530'], ['Martha', '2530'], ['Martha', '1610'], ['James', '1530']] 
print(frequentAccess(records2))