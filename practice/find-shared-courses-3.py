'''
Students may decide to take different "tracks" or sequences of courses in the Computer Science curriculum. There may be more than one track that includes the same course, but each student follows a single linear track from a "root" node to a "leaf" node. In the graph below, their path always moves left to right.

Write a function that takes a list of (source, destination) pairs, and returns the name of all of the courses that the students could be taking when they are halfway through their track of courses.

Sample input:
all_courses = [
    ["Logic", "COBOL"],
    ["Data Structures", "Algorithms"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "COBOL"],
    ["Intro to Computer Science", "Data Structures"],
    ["Logic", "Compilers"],
    ["Data Structures", "Logic"],
    ["Creative Writing", "System Administration"],
    ["Databases", "System Administration"],
    ["Creative Writing", "Databases"],
    ["Intro to Computer Science", "Graphics"],
]

Sample output (in any order):
          ["Data Structures", "Creative Writing", "Databases", "Intro to Computer Science"]

All paths through the curriculum (midpoint *highlighted*):

*Intro to C.S.* -> Graphics
Intro to C.S. -> *Data Structures* -> Algorithms -> COBOL
Intro to C.S. -> *Data Structures* -> Logic -> COBOL
Intro to C.S. -> *Data Structures* -> Logic -> Compiler
Creative Writing -> *Databases* -> System Administration
*Creative Writing* -> System Administration
Creative Writing -> *Data Structures* -> Algorithms -> COBOL
Creative Writing -> *Data Structures* -> Logic -> COBOL
Creative Writing -> *Data Structures* -> Logic -> Compilers

Visual representation:

                    ____________
                    |          |
                    | Graphics |
               ---->|__________|
               |                          ______________
____________   |                          |            |
|          |   |    ______________     -->| Algorithms |--\     _____________
| Intro to |   |    |            |    /   |____________|   \    |           |
| C.S.     |---+    | Data       |   /                      >-->| COBOL     |
|__________|    \   | Structures |--+     ______________   /    |___________|
                 >->|____________|   \    |            |  /
____________    /                     \-->| Logic      |-+      _____________
|          |   /    ______________        |____________|  \     |           |
| Creative |  /     |            |                         \--->| Compilers |
| Writing  |-+----->| Databases  |                              |___________|
|__________|  \     |____________|-\     _________________________
               \                    \    |                       |
                \--------------------+-->| System Administration |
                                         |_______________________|

Complexity analysis variables:

n: number of pairs in the input

'''

'use strict'


def halfway_courses(courses):
    prereqs = {}
    courses_set = set()
    
    # Build a dictionary of prerequisites for each course
    for source, dest in courses:
        prereqs.setdefault(dest, set()).add(source)
        courses_set.add(source)
        courses_set.add(dest)
    
    # Find all the leaf nodes in the graph
    leaf_nodes = courses_set - set(prereqs.keys())
    
    halfway = len(leaf_nodes) // 2
    
    # Perform a breadth-first search starting at each leaf node
    # until we have visited halfway many nodes
    halfway_courses = set()
    for node in leaf_nodes:
        queue = [node]
        visited = set()
        while queue and len(visited) < halfway:
            curr_node = queue.pop(0)
            visited.add(curr_node)
            if curr_node in prereqs:
                for prereq in prereqs[curr_node]:
                    if prereq not in visited:
                        queue.append(prereq)
        if len(visited) == halfway:
            halfway_courses.add(node)
    
    return halfway_courses




allCourses = [
  ['Logic', 'COBOL'],
  ['Data Structures', 'Algorithms'],
  ['Creative Writing', 'Data Structures'],
  ['Algorithms', 'COBOL'],
  ['Intro to Computer Science', 'Data Structures'],
  ['Logic', 'Compilers'],
  ['Data Structures', 'Logic'],
  ['Creative Writing', 'System Administration'],
  ['Databases', 'System Administration'],
  ['Creative Writing', 'Databases'],
  ['Intro to Computer Science', 'Graphics'],
]

print(halfway_courses(allCourses))
