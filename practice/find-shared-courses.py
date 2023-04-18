# You are a developer for a university. Your current project is to develop a system for students to find courses they share with friends. 
# The university has a system for querying courses students are enrolled in, returned as a list of (ID, course) pairs.
# Write a function that takes in a list of (student ID number, course name) pairs and returns, for every pair of students, a list of all courses they share.
 
# Sample Input:
# student_course_pairs_1 = [
#   ["58", "Software Design"],
#   ["58", "Linear Algebra"],
#   ["94", "Art History"],
#   ["94", "Operating Systems"],
#   ["17", "Software Design"],
#   ["58", "Mechanics"],
#   ["58", "Economics"],
#   ["17", "Linear Algebra"],
#   ["17", "Political Science"],
#   ["94", "Economics"],
#   ["25", "Economics"],
# ]
 
# Sample Output (pseudocode, in any order):
 
# find_pairs(student_course_pairs_1) =>
# {
#   [58, 17]: ["Software Design", "Linear Algebra"]
#   [58, 94]: ["Economics"]
#   [58, 25]: ["Economics"]
#   [94, 25]: ["Economics"]
#   [17, 94]: []
#   [17, 25]: []
# }

# T: O(n^2 * m)
# M: O(n*m)
def find_pairs(student_course_pairs):

  #create a dict with student id as key and courses as value
  #iterate over it to find the intersections between 2 courses

  id_course_dict = {}  # id : [courses]

  for id, course in student_course_pairs:
    id = int(id)
    if id in id_course_dict:
      id_course_dict[id].append(course)
    else:
      id_course_dict[id] = [course]

  # print(id_course_dict)

  pairs = {}

  #make courses into a set and use intersection
  #key can't be a list, so need to change to a tuple
  for id1, c1 in id_course_dict.items():
    for id2, c2 in id_course_dict.items():

      #if its the same student, pass  // check for other cases
      if id1 == id2 or tuple([id1, id2]) in pairs or tuple([id2, id1]) in pairs:
        continue

      s_pairs = tuple([id1, id2])
      set1 = set(c1)
      set2 = set(c2)
      pairs[s_pairs] = set1.intersection(set2)

      
  ans = ""
  for k, v in pairs.items():
    ans += f'{list(k)}:{list(v)} \n'

  return ans





print(find_pairs([
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]))



    # #create a dic for each student and the courses they are enroled in

    # #check the students that share the same course
    # #add them into a dic list

    # each_student = {}
    # for student_id, course in student_course_pairs:
    #     if int(student_id) in each_student:
    #         each_student[int(student_id)] += [course]
    #     else:
    #         each_student[int(student_id)] = [course]
    # print(each_student)
 


    # ans = {}
    # for s1, c1 in each_student.items():
    #     for s2, c2 in each_student.items():
    #         #here i want to:
    #         #check if i already computed the s1 and s2, if not, check the courses they share and add to the ans


    #         if s1 == s2 or tuple(sorted((s1, s2))) in ans:
    #             continue
    #         else:
    #             ans[tuple(sorted((s1, s2)))] = list(set(c1).intersection(c2))
    