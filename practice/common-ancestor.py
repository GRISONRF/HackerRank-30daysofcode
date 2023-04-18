""" Whether two nodes have a common ancestor. """

""" edges as defined as: [parent, child] 
so if two child have the same parent, they have a common ancestor
"""

def common_ancestor(edges, x, y):

    #create a dict to store the children and their parents
    graph = {}
    for parent, child in edges:
        if child not in graph:
            graph[child] = set()
        graph[child].add(parent)
    
    ancestors1 = set([x])
    ancestors2 = set([y])
    
    while ancestors1:
        node = ancestors1.pop()
        if node in ancestors2:
            return True
        if node in graph:
            for parent in graph[node]:
                ancestors1.add(parent)
            
    while ancestors2:
        node = ancestors2.pop()
        if node in ancestors1:
            return True
        if node in graph:
            for parent in graph[node]:
                ancestors2.add(parent)
    
    return False
    


edges = [[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]]
x= 4
y= 7
print(common_ancestor(edges, x,y)) #false


edges2 = [[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]]
x2 = 4
y2= 5
print(common_ancestor(edges2, x2,y2)) #true

edges1 = [[1,2], [2,3], [3,4]]
x1 = 2
y1 = 4
print(common_ancestor(edges1, x1, y1)) # Output: true


edges2 = [[1,2], [2,3], [3,4]]
x2 = 2
y2 = 5
print(common_ancestor(edges2, x2, y2)) # Output: False


edges3 = [[1,2], [2,3], [3,4], [4,5]]
x3 = 2
y3 = 5
print(common_ancestor(edges3, x3, y3)) # Output: true


edges4 = [[1,2], [2,3], [3,4], [4,5], [5,6]]
x4 = 6
y4 = 2
print(common_ancestor(edges4, x4, y4)) # Output: False









#FASTER APPROACH, O(LOG N) - UNION-FIND

    # directParents = {}
    # for parent, child in edges:
    #     if child in directParents:
    #         directParents[child].add(parent)
    #     else:
    #         directParents[child] = {parent}

    # print(directParents)
    # def findAllParents(e):
    #     result = set()
    #     stack = [e]
    #     while stack:
    #         curr = stack.pop()
    #         parents = directParents.get(curr)
    #         if not parents:
    #             continue
    #         for parent in parents:
    #             if parent in result:
    #                 continue
    #             result.add(parent)
    #             stack.append(parent)
    #     return result

    # parentsOfX = findAllParents(x)
    # parentsOfY = findAllParents(y)
    # for parentOfX in parentsOfX:
    #     if parentOfX in parentsOfY:
    #         return True
    # return False