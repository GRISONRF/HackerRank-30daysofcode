# Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be removed to make the string a palindrome. There may be more than one solution, but any will do. If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.

#palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as madam or racecar.
# example: "bcbc" can return either '0' or '3'

# return index of chac to be removed.
# if no, return -1


#--------------------------#


# 'abcccca'
def palindromeIndex(s):

    #check if string is a palindrome
    if s == s[::-1]:
        return -1

    #iterate throught half of the string and compare elements
    l = len(s)

    for i in range(l // 2): # divided by 2, using // so we have 'whole' numbers  #'abcc' / 4
        if s[i] != s[l - 1 - i]: # comparing the first with the last element. (length - 1) = ultimo elemento, (- index) = pq vai diminuindo/indo proximo ao meio a cada iteration. # if a != a **is is, no next iteration:** if b !=c , then:
            #first condition: if excluding the first element (on the range between the 2 items that didn't match) the rest of the string is a palindrome:
            if s[i+1: l - i] == s[i+1: l - i][::-1]:  #if  excluding b, are the rest of the items the same? ///from c to c //same as: (l-1) = len of string. (- i) = o numero correspondente do s[i], so que quero ir ate exatamente o numero 1, entao +1. 
                #if so, return index of s that we excluded:
                return i
            # now check if we exclude the 'c', will the rest od the items be the same? /// from b to c
            elif s[i:l - 1 - i] == s[i:l - 1 - i][::-1]: #
                #if so, return index of it
                return l-1-i
        return -1



print(palindromeIndex('baa'))
