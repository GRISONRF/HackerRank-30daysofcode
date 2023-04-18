""" Input is an int[][] input, input[0] is the parent of input[1], for example {{1,4}, {1,5}, {2,5}, {3,6}, {6,7}} will form the above graph. The first question is the nodes with either 0 or 1 parents. """


def find_nodes_with_zero_or_one_parents(input):

    # p, c
    par_child = {}  # child: parent
    for p, c in input:
        par_child[c] = par_child.get(c, []) + [p]
    
    # print(par_child)

    ans = []
    for p, c in input:

        if len(par_child[c]) == 1 or c not in par_child:
            ans.append(c)

        # if len(par_child[p]) == 1 or p not in par_child:
        #     ans.append(p)
            
    print(ans)




input = [[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]]

# test case 1: check nodes with 0 parents
expected_output_1 = [1, 2, 3]
find_nodes_with_zero_or_one_parents(input)
# print("Test case 1:")
# print("Expected output:", expected_output_1)
# print("Output:", output_1)
# if output_1 == expected_output_1:
#     print("Test case 1 passed\n")
# else:
#     print("Test case 1 failed\n")

# # test case 2: check nodes with 1 parent
# expected_output_2 = [4, 5, 6, 7]
# output_2 = find_nodes_with_zero_or_one_parents(input)
# print("Test case 2:")
# print("Expected output:", expected_output_2)
# print("Output:", output_2)
# if output_2 == expected_output_2:
#     print("Test case 2 passed\n")
# else:
#     print("Test case 2 failed\n")



"""
LEETCODE QUESTION!!!
 1 Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. 

-> The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:


parentChildPairs = [  (1, 3), (2, 3), (3, 6), (5, 6),
                   (5, 7), (4, 5), (4, 8), (8, 10)  ] 

Write a function that takes this data as input and returns two collections: one containing all individuals with zero known parents, and one containing all individuals with exactly one known parent.

findNodesWithZeroAndOneParents(parentChildPairs) =>
                                  [ [1, 2, 4],    // Individuals with zero parents
                                  [5, 7, 8, 10] 


#return:
# all individuals with no parents
# all individuals with one parent

def zeroOrOne(parentChildPairs):

    # #set to store the asnwers
    # no_parent = set()
    # one_parent = set()

    #map each number to its parents
    parents_map = {}   # child : parents
    for p, c in parentChildPairs:
        parents_map[c] = parents_map.get(c, []) + [p]
    # print(parents_map)

    ans = [[],[]]
    for c, p in parents_map.items():
        if len(parents_map[c]) == 1:
            ans[1].append(c)
        for i in p:
            if i not in parents_map and i not in ans[0]:
                ans[0].append(i) 
    print(ans)



parentChildPairs = [  (1, 3), (2, 3), (3, 6), (5, 6),
                   (5, 7), (4, 5), (4, 8), (8, 10)  ] 
print(zeroOrOne(parentChildPairs)) """