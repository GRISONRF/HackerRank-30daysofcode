""" You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words. """

def find(words, chars):

    #create var to track matching strings
    matching = ""
    #loop through words
    for word in words:
        #create a dict
        char_dict = {}
        #loop through chars and map chars and its frequencies
        for char in chars:
            char_dict[char] = char_dict.get(char, 0) + 1
            # if char in char_dict:
            #     char_dict[char] += 1
            # else:
            #     char_dict[char] = 1

        for i in range(len(word)):    
            #if this letter is not in the chars dict, or the value is less than 1, break
            if word[i] not in char_dict or char_dict[word[i]] < 1:
                break
            #if letter is in dict and value is greater or equal to 1, 
            if word[i] in char_dict and char_dict[word[i]] >= 1:
                #decrement value of map by one
                char_dict[word[i]] -= 1
                #if curr letter is the last letter of word, add word to string result
                if i == len(word) - 1:
                    matching += word
    return len(matching)







words = ["cat","bt","hat","tree"]
chars = "atach"
words2 = ["hello","world","leetcode"]
chars2 = "welldonehoneyr"
            
print(find(words, chars))
print(find(words2, chars2))