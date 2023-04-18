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

#Time: O(n^2 * 2^n)
#Memory: O(n^2 * 2^n)

def find_longest_chain(songs, song_1):

    #list to store chains
    chains = []

    #create func to build the chain using the chain and the used _songs
    def build_chain(chain, used_songs):

        #get the last word in chain 
        last_word = chain[-1].split()[-1]
        #iterate over the songs
        for song in songs:
            #if the song wasn't used before and the last word from chain == to the first word from curr song
            if song not in used_songs and last_word == song.split()[0]:

                #we will build a chain using the curr chain adding the curr song AND add the song to the set used_songs.
                build_chain(chain + [song], used_songs.union({song}))
        # when the for loop is done, means what we have in the chain is the longest chain we could have made, so add it in the chains
        chains.append(chain)

    #iterate over songs 
    for song in songs:
        
        #if the curr song is equal to the start_song, we build the chain using the song as the first chain and add song in the set of used_songs
        if song == song_1:
            build_chain([song], {song})
    
    #find max len by checking the len of all chains in chains
    max_length = max(len(chain) for chain in chains)  #max_len == number
    #getting the list that has the len == to the max_len
    longest_chains = [chain for chain in chains if len(chain) == max_length]
    
    return longest_chains #return that chain




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






""" 
wronf function signature
def longest_chain(songs):

    chains = {}
    for i in range(len(songs)):
        chain = [songs[i]]
        used_songs = {i}
        for j in range(len(songs)):
            if j not in used_songs and chain[-1].split()[-1] == songs[j].split()[0]:
                chain.append(songs[j])
                used_songs.add(j)
        chains[len(chain)] = chain
    print(chains[max(chains)]) """