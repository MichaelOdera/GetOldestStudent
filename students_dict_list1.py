students = []
def add_student(student):
	students.append(student)
# def oldest_student():
# oldest = students[0]["age"];
# 	for student in students[i]:
# 		if students[i]["age"]>oldest:
# 			return student[i] 
# 		else:
# 			return oldest
def oldest_student(students):
	oldest = 0
	for student in students:
		if student['age'] > oldest:
			oldest = student['age']
	return oldest

def student_lang(lang):
	for student in students:
		if lang in student['lan']:
			return student['name']


a = {"name":"Michael", "lan":["Rubby", "Python", "Java"], "age":132 }
b = {"name":"Christopher", "lan":["Rubby", "Python", "Java"], "age":243} 
add_student(a)
add_student(b)
student_lang("Python")
# comment
print oldest_student(students)