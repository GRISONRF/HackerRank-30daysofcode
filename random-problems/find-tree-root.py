""" given a list of nodes, find the tree root """

# nodes = [1,2,3,4,5,6]
#assume each node has a parent attribute that refers to its parent node in the tree

#nodes = list of nodes
import queue
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right

# def get_root(nodes):
#     #FIND THE NODE WITH THE MOST NUMBER OF CHILDREN

#     #if nodes is empty, return none
#     if not nodes:
#         return None
    
#     #create a dict to store the visited nodes
#     visited_nodes = set()
#     #initialize the root no None
#     root = None

#     #iterate the list of nodes to see if current node has been visited before,
#     for current_node in nodes:
#         #if the current node is not in the dictionary, traverse the children of this node -> the traverse function will traverse the left and right of the node and append in the visited_nodes. 

#         if current_node not in visited_nodes:
#             traverse(visited_nodes, current_node)
#             #set the root as the current node
#             root = current_node
#         #check if the 
#         if len(visited_nodes) != len((nodes)):
#             root = None
#     return root


# def traverse(visited_nodes, current_node):

#     if current_node:
#         if current_node not in visited_nodes:
#             visited_nodes.add(current_node)
#             traverse(visited_nodes, current_node.left)
#             traverse(visited_nodes, current_node.right)




# root: no node's children
# iterate through tree and store children in a set/dict
# at the end, after it iterates through all nodes in the list, compare the nodes in the children variable and the initial list, the node that's not there is the root


# queue = []  #visited 
# 
# 
# 

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findRoot(nodes):
   
    parent = {}
    root_candidates = set(nodes)
    for node in nodes:
        if node.left:
            parent[node.left] = node
            root_candidates.discard(node.left)
        if node.right:
            parent[node.right] = node
            root_candidates.discard(node.right)
    for candidate in root_candidates:
        if candidate.left or candidate.right:
            print(candidate.value)
    return None

          
# create some nodes
node2 = Node(2)
node3 = Node(3)
node1 = Node(5)
node4 = Node(4)
node5 = Node(8)
node6 = Node(5)
node7 = Node(7)
node8 = Node(0)



# link the nodes together to form a tree
node1.left = node2
node1.right = node3
node3.left = node4


# create a list of all the nodes
nodes = [node3, node2, node1, node4,node5,node6,node7,node8 ]

# call the get_root function
root = findRoot(nodes)

# print the root
# print(root.value)