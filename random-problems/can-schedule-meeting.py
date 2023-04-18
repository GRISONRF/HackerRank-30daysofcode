# Question 1: Similar to meeting rooms, the input is an int[][] meetings, int start, int end, each number is time, 13:00 = "1300, 9:30 =" 18930, see the new meeting function cannot be scheduled to meetings 
# ex: {[1300, 1500], [930, 1200],[830, 845]}, new meeting[820, 830], return true; [1450, 1500] return false;



def can_schedule_meeting(meetings, start, end):

    for meeting in meetings:
        print(meeting)
        print(start, end)
        if (
            (start[0] >= meeting[0] and start[0] < meeting[1]) or
            (end[0] > meeting[0] and end[0] <= meeting[1]) or
            (start[0] < meeting[0] and end[0] > meeting[1])
        ):
            return False
    return True

print(can_schedule_meeting(
    [[1300, 1500], [930, 1200], [830, 845]], [820], [830]))  # -> True
print(can_schedule_meeting(
    [[1300, 1500], [930, 1200], [830, 845]], [1450], [1500]))  # -> False
