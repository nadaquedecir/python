
python = {"Ana", "Pedro", "Juan", "Ben", "Camilo"}
java = {"Hugo", "Simon", "Ignacia", "Patrico", "Pablo", "Juan"}

two_courses = python.intersection(java)
print(two_courses)

students_python = python.difference(java)
print(students_python)

all_students = python.union(java)
print(all_students)