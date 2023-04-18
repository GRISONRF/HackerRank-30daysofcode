""" 
You are running a classroom and suspect that some of your students are passing around the answer to a multiple-choice question disguised as a random string.

Your task is to write a function that, given a list of words and a string, finds and returns the word in the list that is scrambled inside the string, if any exists. 
If none exist, it returns the result "-" as a string. There will be at most one matching word. The letters don't need to be in order or next to each other. The letters cannot be reused.

Example:  
words = ["baby", "referee", "cat", "dada", "dog", "bird", "ax"]
string1 = "ctay"
find(words, string1) => "cat"   (the letters do not have to be in order)  
  
string2 = "bcanihjsrrrferet"
find(words, string2) => "cat"   (the letters do not have to be together)  
  
string3 = "tbaykkjlga"
find(words, string3) => "-"     (the letters cannot be reused) 

"""
#T: O(nm) n=len oflist of words / m=max. len of word in the list
#M: O(n) = dictionaty

def scramble(words, stg):

   

    string_chars = {}
    for c in stg:
        if c in string_chars:
            string_chars[c] += 1
        else:
            string_chars[c] = 1

    # Iterate through the words in the list
    for word in words:
        # Convert the word to a dictionary mapping characters to their frequencies
        word_chars = {}
        for c in word:
            if c in word_chars:
                word_chars[c] += 1
            else:
                word_chars[c] = 1

        # Check if all the characters in the word are present in the string
        # (regardless of order) and if their frequencies are less than or equal to the frequencies in the string
        is_match = True
        for c, count in word_chars.items():
            if c not in string_chars or string_chars[c] < count:
                is_match = False
                break
 
        if is_match:
            # If the word is present in the string, return it
            return word

    # If no word was found, return "-"
    return "-"
           
    
    


words = ["baby", "referee", "cat", "dada", "dog", "bird", "ax"]
string1 = "ctay"
string2 = "bcanihjsrrrferet"
string3 = "tbaykkjlga"
print(scramble(words, string1))
print('\n')
print(scramble(words, string2))
print('\n')
print(scramble(words, string3))


""" A grid of characters is given, we can move only one step right or one step down from current position,
Suppose you are at ( i, j ), we can go to either ( i, j+1 ) or ( i+1, j)
char[][] grid1 = {
{'c', 'c', 'x', 't', 'i', 'b'},
{'c', 'c', 'a', 't', 'n', 'i'},
{'a', 'c', 'n', 'n', 't', 't'},
{'t', 'c', 's', 'i', 'p', 't'},
{'a', 'o', 'o', 'o', 'a', 'a'},
{'o', 'a', 'a', 'a', 'o', 'o'},
{'k', 'a', 'i', 'c', 'k', 'i'}
};
Given a string, we need to find out of the coordinates of the string from start to end if it exists in the grid;
class Coordinate {
    int x, y;

    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
	public static boolean found = false;

    private static void dfs(char[][] arr, String str, int index, int i, int j, int r, int c, List<Coordinate> list) {
        if (!found && (i < 0 || j < 0 || i >= r || j >= c || arr[i][j] == '*' || arr[i][j] != str.charAt(index)))
            return;
        list.add(new Coordinate(i, j));
        char ch = arr[i][j];
        arr[i][j] = '*';
        if (index == str.length() - 1) {
            found = true;
            return;
        }
        if (!found)
            dfs(arr, str, index + 1, i + 1, j, r, c, list);
        if (!found)
            dfs(arr, str, index + 1, i, j + 1, r, c, list);
        if (!found)
            arr[i][j] = ch;
        if (!found)
            list.remove(list.size() - 1);
    }

    private static List<Coordinate> find_word_location(char[][] arr, String str) {
        found = false;
        List<Coordinate> list = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                if (arr[i][j] == str.charAt(0))
                    dfs(arr, str, 0, i, j, arr.length, arr[i].length, list);
                if (!list.isEmpty())
                    return list;
            }
        }
        return list;
    } """

""" Given a list of [name, time], where the time is in string format: '1300' // 1 PM in the afternoon.

return: list of names and the times where their swipe badges within one hour. if there are multiple intervals that satisfy the condition, return any one of them.
name1: time1, time2, time3...
name2: time1, time2, time3, time4, time5...
example:
input: [['James', '1300'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1530']] 
output: {
'Martha': ['1600', '1620', '1530']
}

"""
""" 
map the person : times
    -change the time to a string

-create an ans =[] to store the name and times
iterate over the map
    -sort the time

    -create a list with times for when they have a 1h difference
    for loop on times
        -for each person's time, check if the times are within a 1h difference. 
            -if they are, add the time to the list for times
            

"""

