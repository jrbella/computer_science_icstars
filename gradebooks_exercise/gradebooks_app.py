last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]
s_length = len(subjects)
g_length = len(grades)


#add subjects and grades
def add_subject(subject, grade):
  subjects.append(subject)
  grades.append(grade)
  return subject, grade

add_subject('computer science', 100)
add_subject('visual arts', 93)
#Gradebook
gradebook = []
if s_length == g_length:
  gradebook = zip(subjects, grades)
print(list(gradebook))
#else statement for block above
#print("Objects do not match there are too many, subjects: " + str(s_length) + grades: " + str(g_length))

full_gradebook = list(gradebook) + last_semester_gradebook
print(full_gradebook)