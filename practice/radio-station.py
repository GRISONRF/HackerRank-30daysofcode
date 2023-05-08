"""  Our local radio station is running a show where the songs are ordered in a very specafic way. The last word of the
"Salent Running" could be
title of one song must match the first word of the title of the next song - for example,
No song may be played more than once.
followed by "Running to Stand Still".

4 Given a list of songs and a starting song, find the longest chain of sings that begins with that song, and the last
Write a function that returns the longest such chain.
word of each song title matches the first word of the next one.
If multiple equivalent chains exist, return any of them

6 Example:
songst = I "Down By the River" "River of Dreams","Take me to the River""Dreams","Blues Hand Me Down", "Forever Young"
«American Dreams""All My Love""Cantaloop","Take it All""Love is Forever" "Young American" "Every Breath You Take" 
song1_1 = "Every Breath You Take"
chaining (songs1, song1_1) > ['Every Breath You Take "Take It All', 'All My Love, "Love is Forever Forever
Young', 'Young American", "American Dreams", "Dreams' ]

25 Additional Input:
26 sOng1_2 = "Dreams"
27 Songi 3 = "Blues Hand Me Down"
28 song1_4 - "Cantaloop"

30 songs2 = [

Nothing at All"
"Money for Nothing"
"Love Me Do"
Do vou Feel Like We DO
"вуе вуе вуе"
Do You Believe in Magic
"вуе вуе Baby """

def find_longest_chain(songs, song1_1):

    #map to store songs
    mapping = {}
    #iterate over songs
    for song in songs:
        #split them
        mapping[song] = song.split()

    #helper funtion to get the longest chain // takes the current song and the curr chain
    def get_longest_chain(current_song, current_chain):
        #update the longest chain to be the current
        longest_chain = current_chain
        #get current last word which will be the last word from the last song of the current chain
        current_last_word = current_song.split()[-1]

        #iterate over the mapping
        for song, words in mapping.items():
            #check if the song isnt already in the current chain and if the first word of the song's word is same as curr last word
            if song not in current_chain and words[0] == current_last_word:
                #if it is, thats the next song in the chain, so we get the longest chain using the song and the current chain + [song]
                next_chain = get_longest_chain(song, current_chain + [song])
                #at the end of the chain, check which chain is the longest and update
                if len(next_chain) > len(longest_chain):
                    longest_chain = next_chain
        #return the longest
        return longest_chain

    #call the longest chain with the first song
    return get_longest_chain(song1_1, [song1_1])

#T: O(n^2 * m)  recursion, loop, N = num of songs. M= len of each title // N^2 for every song we iterate over all of the songs. * M = go over each song and split the words, so it depends on the len of the song. ANSWER = O(n^2 * m)
#M: N*M -> map size of the num of songs. since it stores the words, it can have at most M length





songs = [
    "Down By the River",
    "River of Dreams",
    "Take me to the River",
    "Dreams",
    "Blues Hand Me Down",
    "Forever Young",
    "American Dreams",
    "All My Love",
    "Cantaloop",
    "Take it All",
    "Love is Forever",
    "Young American",
    "Every Breath You Take"
]

song1_1 = "Every Breath You Take"
song1_2 = "Dreams"
song1_3 = "Blues Hand Me Down"
song1_4 = "Cantaloop"

print(find_longest_chain(songs, song1_1))
print(find_longest_chain(songs, song1_2))
print(find_longest_chain(songs, song1_3))
print(find_longest_chain(songs, song1_4))


