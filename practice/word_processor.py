""" 
We are building a word processor and we would like to implement a "reflow" functionality that also applies full justification to the text.
Given an array containing lines of text and a new maximum width, re-flow the text to fit the new width. Each line should have the exact specified width.
If any line is too short, insert '-' (as stand-ins for spaces) between words as equally as possible until it fits.
Note: we are using '-' instead of spaces between words to make testing and visual verification of the results easier.

lines = [ "The day began as still as the",
          "night abruptly lighted with",
          "brilliant flame" ]

reflowAndJustify(lines, 24) ... "reflow lines and justify to length 24" =>

        [ "The--day--began-as-still",
          "as--the--night--abruptly",
          "lighted--with--brilliant",
          "flame" ] // <--- a single word on a line is not padded with spaces
"""

def word_processor(lines, max_len):
    
    words = ' '.join(lines).split()
    result = []
    i = 0

    #iterate over all words in the list while still on bounds
    while i < len(words):
        #split words into lines
        #remain is what is left in that line, so we start as the max_len since there's no word there
        remain = max_len
        count = 0 #count how many words are in this line

        #another loop to figure how many words +1 fit in this line
        while i < len(words):
            if remain - len(words[i]) < 0: #if remain becomes negative, we know we reached the end of line
                break

            count +=1
            remain -= len(words[i]) + 1 #remain - the word + dash
            i+=1
        line = words[i - count:i] #creates a slice of the words from index of i - count until index o i. which means its extracting each line of a time. because count is how many words fit in that line and i is the index of the first word that doesn't fit in that line.

        #now, calculate how many dashes between each word:

        n = sum(len(word) for word in line) # total len of words in the line excluding the spaces between the words
        baseDash = '-' * ((max_len - n) // (len(line) - 1)) if len(line) > 1 else '' #calculates the required number of dashes between each word: max len - len of all words of line // by len of line - 1
        extra = (max_len - n) % (len(line) - 1) if len(line) > 1 else 0 #stores the number of extra dashes required at the beginning of the line. take the remainder of the subtraction of the len of words in the line from the max len allowed and dividing the result by the number of words in the line minus 1
        reflowed = '' #line result with padded dashes

        for j, word in enumerate(line):
            if j == len(line) - 1:
                reflowed += word
            else:
                reflowed += word + baseDash + ('-' if extra > 0 else '')
                extra -= 1
        result.append(reflowed)
    return result





lines = [ "The day began as still as the",
          "night abruptly lighted with",
          "brilliant flame" ]
width = 24
print(word_processor(lines, width))

""" def word_processor(lines, max_len):

    if not lines or len(lines) == 0:
        return []

    words = ' '.join(lines).split()
    result = []
    i = 0
    while i < len(words):
        # split words into lines first
        remain = max_len
        count = 0

        while i < len(words):
            if remain - len(words[i]) < 0:
                break
            count += 1
            remain -= len(words[i]) + 1
            i += 1

        line = words[i - count:i]
        # after splitting into lines, calculate the required dashes between each word
        n = sum(len(word) for word in line)
        baseDash = '-' * ((max_len - n) // (len(line) - 1)) if len(line) > 1 else ''
        extra = (max_len - n) % (len(line) - 1) if len(line) > 1 else 0  # some dashes at the beginning has one extra dash
        reflowed = ''  # line result with padded dashes
        for j, word in enumerate(line):
            if j == len(line) - 1:
                reflowed += word
            else:
                reflowed += word + baseDash + ('-' if extra > 0 else '')
                extra -= 1
        result.append(reflowed)
    return result """