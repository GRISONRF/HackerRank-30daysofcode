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


#list to store the longest sequence -> dont store the len, store the strings

#iterate over user0
#iterate over user1
    #create a list for temp max
    #check if string at user0 is at user1. if it is:
        
        #start a while loop to iterate over user0 while next of both users are the same.

        #when while loop is done /when not the same
        #check if the temp max subarray > max subarray
    #return max subarray

def findContiguousHistory(user1, user2):

    max_seq = []

    for i in range(len(user1)):
        temp_max_seq = []
        for j in range(len(user2)):

            if user1[i] == user2[j]:
                temp_max_seq.append(user1[i])   

                #on bounds of user1 and 2 and while next from user 1 == next from user2
                while i+1 < len(user1) and j+1 < len(user2) and user1[i+1] == user2[j+1]:
                    temp_max_seq.append(user1[i+1])
                    i+=1
                    j+=1
                
                if len(max_seq) < len(temp_max_seq):
                    max_seq = temp_max_seq
                
                temp_max_seq = []
    print(max_seq)
           
print(findContiguousHistory(user3,user6))