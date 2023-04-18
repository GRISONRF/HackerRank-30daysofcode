""" output intermediate courses """

def find_midway(prereqs):

    #initialize emprt list for result
    result = []

    #creates a set with all the courses that are the prequequisits courses // ex:  ['Data Structures', 'Algorithms'], the prerequisit is Algorithms 
    courses_have_prereq = set()
    for prereq in prereqs:
        courses_have_prereq.add(prereq[1])
    # print(courses_have_prereq)
    

    #look trough the prerequisits again, and look for the course that has NO prerequesit. that means this is the FIRST course.
    #when we find one, add to the curr and break from the loop
    curr = None
    for prereq in prereqs:
        if prereq[0] not in courses_have_prereq:
            curr = prereq[0]
            break

    #create a list called courses that includes all the courses that have prerequisits and the course stored in curr
    courses = list(courses_have_prereq)
    courses.append(curr)

    # we know both result and courses need to have the same length
    #this function creates the result list, which is the order of the courses and its prerequisits. 
    #so while we dont have all the courses in the result, we append the curr to the result at each iteration
    while len(result) != len(courses):
        result.append(curr)
        #iterate through the prerequisit list again
        for prereq in prereqs:
            
            #if the current course is equal to the first prerequisite
            if curr == prereq[0]:
                #we change the curr to be the prerequisite to it
                curr = prereq[1]
                break
    
    #this while loop takes the course and find it prerequisite. then it changes the curr course to be the prerequisite and keeps going until find the last course that has no prerequisite. that makes the result to have the courses in the order of prerequisites.

    #now to return the course in the middle, we need to find the middle of the list
    if len(result) % 2 == 0:
        return result[int(len(result) // 2)]

    return result[int(len(result) / 2)]
    


prereqs_courses1 = [
  ['Data Structures', 'Algorithms'],
  ['Foundations of Computer Science', 'Operating Systems'],
  ['Computer Networks', 'Computer Architecture'],
  ['Algorithms', 'Foundations of Computer Science'],
  ['Computer Architecture', 'Data Structures'],
  ['Software Design', 'Computer Networks'],
]

# prereqs_courses2 = [
#   ['Data Structures', 'Algorithms'],
#   ['Algorithms', 'Foundations of Computer Science'],
#   ['Foundations of Computer Science', 'Logic'],
# ]

# prereqs_courses3 = [['Data Structures', 'Algorithms']]

print(find_midway(prereqs_courses1))
# print(find_midway(prereqs_courses2))
# print(find_midway(prereqs_courses3))







