""" . The input is an int[][] meetings and int start, int end, each time is represented as an integer.
For example, 13:00 = 1300 and 9:30 = 930. 
The question is whether the new meeting can be arranged within the existing meetings.

Example:
input: [[1300, 1500], [930, 1200], [830, 845]], new meeting [820, 830], return true; [1450, 1500] return false. """


def meetingRooms(meetings, start, end):

    # sorted_meetings = sorted(meetings)
    # print(sorted_meetings)

    if not meetings:
        return True

    for meeting in meetings:
        print(meeting)

        #false:
        #if start after or the same time as start
        if start >= meeting[0] and start < meeting[1] or end > meeting[0] and end <= meeting[1] or start < meeting[0] and end > meeting[1]:
            return False

        else:
            return True










meetings = [[1300, 1500], [930, 1200],[830, 845]]
start = 820
end = 830  #true

# meetings = [[1300, 1500], [930, 1200],[830, 845]]
# start = 1450
# end = 1500 #false


# meetings = []
# start = 1000
# end = 1100 #true


# meetings = [[1300, 1500], [930, 1200],[830, 845]]
# start = 1300
# end = 1500  #false

# print(meetingRooms(meetings, start, end))



""" PART 2
Return the free time intervals.

Similar to merge intervals, the only difference is the output. The output is the free time period. After merging, output the empty spaces between each of them, and remember to add 0 to the start time of the first one.

merge intervals:Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

"""

def spareTime(intervals):

    
    if len(intervals) == 0:
        return []
    s_intervals = sorted(intervals)
    res = []
    start = 0

    for interval in s_intervals:

        if start < interval[0]:
            res.append([start, interval[0]])
            
        start = max(start, interval[1])
    res.append([start, 1440])
    return res




# Test case 1
intervals = [[820, 830], [1300, 1500], [930, 1200], [830, 845]]
print(spareTime(intervals)) # Output: [[0, 820], [830, 830], [1500, 1500]]

# Test case 2
intervals = [[820, 830], [1300, 1500], [930, 1200]]
print(spareTime(intervals)) # Output: [[0, 820], [1500, 1500]]

# Test case 3
intervals = [[820, 830], [1300, 1500]]
print(spareTime(intervals)) # Output: [[0, 820], [1500, 1500]]

# Test case 4
intervals = [[820, 900]]
print(spareTime(intervals)) # Output: [[0, 820], [900, 900]]

# Test case 5
intervals = []
print(spareTime(intervals)) # Output: []