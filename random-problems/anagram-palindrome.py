from collections import Counter


def anagramPalindrome(str):



    a = Counter(str)

    odd = 0

    for v in a.values():
        if v%2==1:
            odd+=1
    print(odd)
    
    if odd > 1:
        return False
    else: return True



print(anagramPalindrome("a"))
print(anagramPalindrome(""))
