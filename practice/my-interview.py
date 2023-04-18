'''
We have some clickstream data that we gathered on our client's website. We collected snippets of users' anonymized URL histories while they browsed the site. The histories are in chronological order, and no URL was visited more than once per person.

Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.

Sample input:

user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

Sample output:

findContiguousHistory(user0, user1) => ["/pink", "/register", "/orange"]
findContiguousHistory(user0, user2) => [] (empty)
findContiguousHistory(user0, user0) => ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
findContiguousHistory(user2, user1) => ["a"] 
findContiguousHistory(user5, user2) => ["a"]
findContiguousHistory(user3, user4) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user4, user3) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user3, user6) => ["/tan", "/red", "/amber"]
findContiguousHistory(user6, user3) => ["/tan", "/red", "/amber"]

n: length of the first user's browsing history
m: length of the second user's browsing history
'''

user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

# Note: built-in functions like the Python difflib module should not be used as solutions to this problem

def findContiguousHistory(user1, user2):
    
     #user1 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
     #user2 = ["/start", "/pink", "/register", "/orange", "/red", "a"]


    # result = []
    # max_len = 0

    # for i in range(len(user1)):
    #     for j in range(len(user2)):

    #         records = []
            
    #         k = 0
    #         while (i+k < len(user1)) and (j+k < len(user2)) and user1[i+k] == user2[j+k]:
    #             # print(user1[i+k])
    #             records.append(user1[i+k]) 
    #             k +=1
            
    #         if len(records) > max_len:
    #             # print(records)
    #             result.append(records)
    #             max_len = len(records)
                
    # # return result
    # # print(result)


    result = []
    max_len = 0
    
    #iterate over user0
    for i1 in range(len(user1)): # i1 =0
        
        #creating list to temp max
        
        #iterate over user1
        for i2 in range(len(user2)): #i2 = 0
            # print(user1[i1])
            maybe_max = []
            
            #check if str1 == str2
            if user1[i1] == user2[i2]:   
                #if they're the same, add to maybe_max and start checking the next strings
                    #while str1+1 == str2+1 and on bounds
                j = 0
                while i2 + j < len(user2) and i1 + j < len(user1) and user1[i1 + j] == user2[i2 + j]: 
                    #add to maybe max\
                    maybe_max.append(user1[i1 + j])
                    #increment j+1
                    j +=1

                #update max_len
                if len(maybe_max) > max_len:
                    #max_len =  max between len of max_len and maybe_max
                    result = maybe_max
                    max_len = len(maybe_max)
    print(result)


print(findContiguousHistory(user3, user4))

    # #create a set with user 1
    # set1 = set(user2)

    # #store the max total / result
    # max_l = []

    # #iterate over user2
    # for i in range(len(user2)):

    #     potencial_max = []
    #     #if cur string is present in other user list
    #     if user2[i] in set1:

    #         # add it to potential max
    #         potencial_max.append(user2[i])

    #         #sliding window kinda of? -> i want to iterate over both 
    #         j=0
    #         for j in range(len(i+j, len(user2))):
    #             if user2[i+j] == user2[]








    # max_len = []
    
    # #iterate over user1
    # for i1 in range(len(user1) -1): # i1 =0
        
    #     #creating list to temp max
    #     maybe_max = []
        
    #     #iterate over user2
    #     for i2 in range(len(user2)): #i2 = 0
    #         # print(user1[i1])
            
    #         #check if str1 == str2
    #         if user1[i1] == user2[i2]:   
    #             #if they're the same, add to maybe_max
    #                 #while str1+1 == str2+1
    #                 j = 0
    #                 while i2 + j < len(user2) and i1 + j < len(user1) and user1[i1 + j] == user2[i2 + j]: 
    #                     #add to maybe max\
    #                     maybe_max.append(user1[i2 + j])
    #                     #increment j+1
    #                     j +=1
    #                 #update max_len
    #                 max_len = max(max_len, maybe_max)
    #     print(maybe_max)
                
                   
                
        
        #max_len = max(max_len, mmaybe)
    
    
    
   


# print(findContiguousHistory(user0, user1))














#create a map with domain as key and count as the value
    # iterate over the list
        #split "," count, domain = ['google', 'com']
        #
        
from collections import defaultdict
        
def calculateClicksByDomain(counts):
    
    domain_count_map = defaultdict(int)
    
    for domain in counts:
        count, domain = domain.split(',')
        
        count = int(count)
        subdomain = domain.split('.')
        
        for i in range(len(subdomain)):


            domain_count_map[".".join(subdomain[i:])] += count
        
    return domain_count_map


counts = [
    "900,google.com",
    "60,mail.yahoo.com",
    "10,mobile.sports.yahoo.com",
    "40,sports.yahoo.com",
    "300,yahoo.com",
    "10,stackoverflow.com",
    "20,overflow.com",
    "5,com.com",
    "2,en.wikipedia.org",
    "1,m.wikipedia.org",
    "1,mobile.sports",
    "1,google.co.uk" 
]


# print(calculateClicksByDomain(counts))






'''
For a new autocorrect system, we want to find the relationships between frequently typed in words and similar words that are one letter longer.

Given two strings s1 and s2, we will call (s1, s2) a "step" if you can form s2 by adding exactly one letter to s1 and possibly rearranging the letters of s1.

For example:
(OF, FOR) is a step
(OF, IF) is not a step
(OF, OCT) is not a step
(ERA, EAR) is not a step
(SHE, SHEEP) is not a step
(TEE, TEST) is not a step

Given a wordlist, produce an index of possible one-letter steps
   w -> {  w1 | (w, w1) is a step } 
that associates to each word all the words in the wordlist that are a step away from it.

wordlist = [
  ["OF",   "30966074"],
  ["FOR",   "6545282"],
  ["NO",    "6545282"],
  ["ON",    "4594521"],
  ["NOT",   "4522732"],
  ["FROM",  "3469207"],
  ["ONE",   "2148983"],
  ["INTO",  "1144226"],
  ["OUGHT",  "785433"],
  ["THOUGH", "785433"],
  ["SOUGHT", "785433"],
  ["THOUGHT","785433"],
  ["NOW",    "679337"],
  ["FOUR",   "679337"],
  ["FORM",   "352032"],
  ["OFF",    "333858"],
  ["POINT",  "333858"],
  ["LEFT",   "306802"],
  ["FORMS",  "136468"]
]

one_letter_steps_index = step_index(wordlist)

# Expected output (pseudocode, unordered):

NO     : [ ONE, NOT, NOW ]
INTO   : [ POINT ]
LEFT   : []
FORM   : [ FORMS ]
ONE    : []
FOUR   : []
FOR    : [ FORM, FOUR, FROM ]
FROM   : [ FORMS ]
OFF    : []
OUGHT  : [ THOUGH, SOUGHT ]
SOUGHT : []
THOUGH : [ THOUGHT ]
THOUGHT: []
FORMS  : []
NOT    : [ INTO ]
OF     : [ FOR, OFF ]
NOW    : []
POINT  : []
ON     : [ ONE, NOT, NOW ]

Complexity analysis variables:  
  
N = The number of words  
L = The length of words  
'''

wordlist = [
    ["OF", "30966074"],
    ["FOR", "6545282"],
    ["NO", "6545282"],
    ["ON", "4594521"],
    ["NOT", "4522732"],
    ["FROM", "3469207"],
    ["ONE", "2148983"],
    ["INTO", "1144226"],
    ["OUGHT", "785433"],
    ["THOUGH", "785433"],
    ["SOUGHT", "785433"],
    ["THOUGHT", "785433"],
    ["NOW", "679337"],
    ["FOUR", "679337"],
    ["FORM", "352032"],
    ["OFF", "333858"],
    ["POINT", "333858"],
    ["LEFT", "306802"],
    ["FORMS", "136468"],
]



def step_index(wordlist):
    
    words = []
    for w, n in wordlist:
        words.append(w)
    
    
    ans = {}  # word : [word + 1 len longer]
    
    #loop over the list of words
    for word in words:
        # temp list of words that match the word i'm cheking
        temp_match = []
        
        # MAP1 create a dict to map frequency of each letter of this word -> O:1, F:1     
        map_word = {}
        for l in word:
            if l not in map_word:
                map_word[l] = 0
            map_word[l] += 1
        
        # iterate over the words again (check case when words are the same /dont)
        for word2 in words:
            if word2 != word and len(word2) == len(word) +1:
                #-> FOR
                #only want to add in the map if len of word == len 1word+1
                map_word2 = {}
                for l2 in word2:
                    if l2 not in map_word2:
                        map_word2[l2] = 0
                    map_word2[l2] += 1                
                
                #MAP2 create a dict to map letter of word [F:1, O:1, R:1]
                
                for l, f in map_word.items():
                #iterate over MAP1 
                    #if this letter in map2
                        #
                
        
    
    
    
    
    
    
print(step_index(wordlist))



# counts = word, frquency
# create a dictionary to map word and freq -> only add the ones that matches len from 2 to X
# sort the items in dict by the frequency



def top(counts, need_words, max_word_length):
    
    map_word_freq = {}
    for item in counts:
        word, count = item.split(',')
        if len(word) >= 2 and len(word) <= max_word_length:
            if word not in map_word_freq:
                map_word_freq[word] = int(count)
     
    sorted_map = sorted(map_word_freq.items(), key=lambda item:item[1], reverse=True)   
    
    ans = []
    count = 0
    for w, f in sorted_map:
        count += 1
        if count <= need_words:
            ans.append(tuple([w, f]))
    return ans
    
    



# print(top(counts1, need_words = 12, max_word_length = 5))
# print(top(counts2, need_words = 1, max_word_length = 3))
# print(top(counts2, need_words = 3, max_word_length = 3))


