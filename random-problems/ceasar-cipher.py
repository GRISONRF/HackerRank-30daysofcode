# Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

# Input Format:
# The first line contains the integer, , the length of the unencrypted string.
# The second line contains the unencrypted string, .
# The third line contains , the number of letters to rotate the alphabet by.

# input: 11 middle-Outz 2
# output: okffng-Qwvb

# the ceaser cipher encryption rule can be expressed madwthematically as: c = (x + n) % 26. c = encoded character, x = actual character, n = number of positions to shit, mod of 26 bc there are 26 letters in the alphabet

# ord() -> method to convert a character to its numeric representation in Unicode.
# chr() -> method to convert a Unicode to the corresponding character.
# can use a chained operattion: c = chr(ord(c)) -> c = 99


#___________________________________________________________________________________________________
# input: middle-Outz 2
# output: okffng-Qwvb



def caesarCipher(s, k):

    alph = 'abcdefghijklmnopqrstuvwxyz'
    alph_upper = alph.upper()
    full_alph = alph + alph_upper
    
    #rotate the alphabet:
    alph_shifted = alph[k:] + alph[:k] + alph_upper[k:] + alph_upper[:k]


    #create a dictionary to store alph and corresponding shifted letter:
    dict_letters = dict(zip(full_alph, alph_shifted))

    #check for letter in the phrase and print shifted corresponding letter
    string_result = ''
    
    for item in s:
        if item in dict_letters:
            string_result += dict_letters[item]
        else:       
            string_result += item
        
    print(alph)
    print(alph_shifted)
    print(dict_letters)
    print(string_result)
            


    
caesarCipher('middle-Outz', 2)

