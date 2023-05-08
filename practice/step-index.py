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



def step_index(wordlist):

    result = {}
    
    #iterates over wordlist
    for i in range(len(wordlist)):
        #word 1
        w1 = wordlist[i][0]
        #add this word as a key to the result with an empty list as value
        result[w1] = []

        #iterate over the word list again
        for j in range(len(wordlist)):
            #if the indexes are the same, ignore
            if i == j:
                continue
            #sava the word into w2
            w2 = wordlist[j][0]

            #if len of both words dont have a 1 diff, ignore
            if len(w2) - len(w1) != 1:
                continue

            #create lists using the words
            w1_chars = list(w1)
            w2_chars = list(w2)
            #check if letters match
            for c in w1_chars:
                if c in w2_chars:
                    w2_chars.remove(c)  #if leter is same, remove
                else:
                    break
            else:
                result[w1].append(w2)
    
    return result






wordlist = [
    ["OF", "30966074"],
    ["ROF", "6545282"],
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

print(step_index(wordlist))