""" there is a list with a list of songs names and it's respective duration in minutes.
you have to return a list containing all the name of songs that together will sum up to 7 minutes. """


def find_songs(songs):


    # min is string -> convert to int, seconds
    # target -> 7 min (seconds)

    #create a dict to store song and secs // secs : song
    #ans = []

    #iterate songs
        # convert min
        # check if target - secs of curr song in dict
        # if it is, add to answer: song name of curr and the one in dict
        # if not, add curr song name and secs in dict
    
    #deal with duplicates
    #7min = 420 secs

    mapping = {}
    ans = []

    for song, min in songs:
        
        m, s = min.split(':')
        secs = (int(m) * 60) + int(s)
        target = 420 #7min = 420 secs
        
        
        if target - secs not in mapping:
            mapping[secs] = song
        else:  
            ans.append([mapping[target - secs], song])
    return ans
        

# O(n) time
# O(n) memory

songs = [['song1', '4:30'],['song2', '2:30'],['song3', '2:20'], ['song4', '4:40'], ['song5', '3:25']] 
#[['song2', 'song1'], ['song4', 'song3']]

# songs = [["song1", "2:30"], ["song2", "3:45"], ["song3", "4:00"], ["song4", "1:15"], ["song5", "2:30"], ["song6", "4:30"]]
# [["song5", "song6"]]


# songs = [["song1", "2:30"], ["song2", "3:00"], ["song3", "1:30"]]
#[]



result = find_songs(songs)
print(result)  



"""    # change the min to int and into seconds

    song_min = {} # min, name
    result = []

    for song, mins in songs:
        min, sec = mins.split(':')
        secs = int(min) * 60 + int(sec)

        #do the same with 7
        target = 7 * 60
        # print(target)
        # print(target - secs)


        if target - secs in song_min:
            result.append([song, song_min[target - secs]])
        
        else:
            song_min[secs] = song
    
    print(result)
    # print(song_min) """