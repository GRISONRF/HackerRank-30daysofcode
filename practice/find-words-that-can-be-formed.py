def cc(words, chars):
    result = set()

    # map chars = { l: frequency }
    chars_map = {}
    for c in chars:
        chars_map[c] = chars_map.get(c, 0) + 1
    # print(chars_map)
    
    #iterate words
    for word in words:
        #for each word, map letteres and frequency
        word_map = {}
        for c in word:
            word_map[c] = word_map.get(c, 0) + 1
        # print(word_map)
        
        for k, v in word_map.items():
        #for each word in the dictionay, check if the value is <= to the same letter in chars dict

            if k in chars_map and v <= chars_map[k]:
            #if it is, add to result
                result.add(word)
    #return len of result
    print(len(result))


words = ["cat","bt","hat","tree"]
chars = "atach"

print(cc(words, chars))