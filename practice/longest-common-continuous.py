""" Input:
[
["3234.html", "xys.html", "7hsaa.html"], // user1
["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"] // user2
]

Output: The longest continuous and identical visit record of two users.
["xys.html", "7hsaa.html"]

Similar to the LCS solution, if the current two strings are equal, the current cell becomes [i-1][j-1] + 1. If they are not equal, it remains 0. """


def longestCommonContinuousHistory(history1, history2):

    #iterate over both arrays

    #find when strings are the same
    #keep track of len
    #whenever len is > max len, update result

    result = []
    max_len = 0

    for i in range(len(history1)):
        for j in range(len(history2)):

            records = []
            
            k = 0
            while (i+k < len(history1)) and (j+k < len(history2)) and history1[i+k] == history2[j+k]:
                print(history1[i+k])
                records.append(history1[i+k]) 
                k +=1
            
            if len(records) > max_len:
                print(records)
                result.append(records)
                max_len = len(records)
                
    return result

            








#Test Case 1
history1 = ["3234.html", "xys.html", "7hsaa.html"]
history2 = ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"]
print(longestCommonContinuousHistory(history1, history2)) # Output: ["xys.html", "7hsaa.html"]

# #Test Case 2
# history1 = ["1.html", "2.html", "3.html", "4.html", "5.html"]
# history2 = ["1.html", "2.html", "3.html", "4.html", "6.html"]
# print(longestCommonContinuousHistory(history1, history2)) # Output: ["1.html", "2.html", "3.html", "4.html"]

# #Test Case 3
# history1 = ["1.html", "2.html", "3.html", "4.html", "5.html"]
# history2 = ["3.html", "4.html", "5.html", "6.html", "7.html"]
# print(longestCommonContinuousHistory(history1, history2)) # Output: ["3.html", "4.html", "5.html"]

# #Test Case 4
# history1 = []
# history2 = ["3.html", "4.html", "5.html", "6.html", "7.html"]
# print(longestCommonContinuousHistory(history1, history2)) # Output: []

# #Test Case 5
# history1 = ["1.html", "2.html", "3.html", "4.html", "5.html"]
# history2 = []
# print(longestCommonContinuousHistory(history1, history2)) # Output: []

# def longestCommonContinuousHistory(history1, history2):

#     #list to store result
#     result = []
#     #max len
#     max_length = 0
#     #iterate over 1 list
#     for i in range(len(history1)):
#         #iterate over 2nd list
#         for j in range(len(history2)):
#             #len = 0
#             length = 0
#             # k is used to iterate over the values of h2. represents index of curr element being considered in h2 list
#             k = 0
#             #first check if i+k is within the bounds of h1 and h2, and if the strings at i/j index + k  are the same
#             while (i + k < len(history1)) and (j + k < len(history2)) and history1[i + k] == history2[j + k]:
#                 #if they're the same, add 1 to len
#                 length += 1
#                 #k + 1 to keep the loop going
#                 k += 1
#             #when loop is done check if len > max_len
#             if length > max_length:
#                 #if it is, update result and update max_len
#                 result = history1[i:i + k] #result is from when both strings started to be equal until when they stoped being the same
#                 max_length = length
#     return result