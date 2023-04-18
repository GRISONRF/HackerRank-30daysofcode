""" Write a function that, given a list of strings, returns a list of characters representing the first character in each string """

# return List<Character> #takes List<String>

def getListOfChars(values):
    lst_char = []
    for c in values:
        lst_char.append(c[0])

    return lst_char

values = ["The", "rain", "Spain", "on", "the", "plain"]
print(getListOfChars(values))


# Write a function that takes a string and returns a string with all the vowels replaced with a *
#return String, takes in a String

def vowelsReplaced(strings):
    ans = ""
    for c in strings:
        if c in 'aeiou':
            ans += "*"
        else:
            ans += c
    return ans

strings = "rafaela"
print(vowelsReplaced(strings))

#Write a function that takes a string and returns a list of unique characters from the string
#returns: List<Character> / takes String

def uniqueChars(string):
    unique  = set()

    for c in string:
        unique.add(c)
    return list(unique)

print(uniqueChars(string="rafaela"))


#Write a function that takes a list of random numbers as well as a single number and returns the largest number in the list smaller than the given number

#return int() // takes List<Integer>, int()

def smallestNum(nums, num):

    smallest = float('-inf')
    for n in nums:
        if n < num and n > smallest:
            smallest = max(smallest, n)
        
    return smallest if smallest != float('-inf') else -1



print(smallestNum(nums=[10, 12, 42, 71, 84, 93, 21], num=2))