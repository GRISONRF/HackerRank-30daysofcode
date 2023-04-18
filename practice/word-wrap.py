""" Given a word list and the maximum length, connect the words using dashes, but do not exceed the maximum length """



def word_wrap(words, max_len):

    ans = []

    temp = ''
    for word in words:
      
        #when temp + word + '-' < max_len
        if len(temp) + len(word) < max_len:
            temp += word + '-'

        #when temp + word + '-'= max_len
        elif len(temp) + len(word) == max_len:
            temp += word
            ans.append(temp)
            temp = ''

        #when temp + word + '-' > max_len
        elif len(temp) + len(word) > max_len:
            temp = temp[:-1]
            ans.append(temp)
            temp = word + '-'

    if temp != '':
        ans.append(temp[:-1])
    print(ans)




print(word_wrap(["The", "day", "began", "as", "still", "as", "the","night", "abruptly", "lighted", "with", "brilliant", "flame"], 13))
#['The-day-began', 'as-still-as', 'the-night', 'abruptly', 'lighted-with', 'brilliant', 'flame']