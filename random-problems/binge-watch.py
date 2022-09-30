""" A friend of Alex has gifted a movie collection, and Alex is excited to watch them all as quickly as possible. The duration of the movies is given in array durations[n]. n is the number of movies, and each movie's duration is between 1.01 and 3.00 units of time (up to two decimal places).
Every day, Alex wants to spend no more than 3.00 units of time watching the movies and to complete the movies in the minimum number
of days possible. If a movie is started, Alex watches the complete movie on the same day. 
Find the minimum number of days needed to watch all the movies.
Example
n=5
durations = [1.90, 1.04, 1.25, 2.5, 1.75]
Considering 1-based indexing, Alex can watch ®
the movies in a minimum of 3 days as:
Day 1: first and second movie: 1.90 + 1,04 =
2.94 s 3.00
- Day 2:
fourth movie: 2.5 ≤ 3.00
Day 3:
third and fifth movies: 1.25 + 1.75 =
3.00 ≤ 3.00 """
# [1.90, 1.04, 1.25, 2.5, 1.75]


def bingeWatching(n):

    # sort the list 
    # create empt dic

    # check if last movie minus 3 is = to the lenght of another movie (that is NOT in the dict yet) or if 2 movies length are = to that.
    #if so, add 1 to days [a dictionary, key=day, value=movie length]
    #return the last key?


    days = {}
    sorted_lengths = sorted(n)
    whats_left = 0

    if sorted_lengths[-1] < 3:
        if (sorted_lengths[-1] - 3) in n and (sorted_lengths[-1] - 3) not in days:
            days[1] = [sorted_lengths, sorted_lengths[-1]]
    print(days)



bingeWatching([1.90, 1.04, 1.25, 2.5, 1.75])