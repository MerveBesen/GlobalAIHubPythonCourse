student = {}
grade = list()
studentGrades = list()

for i in range(5) :
    
    j = list()
    name = input("Name : ")
    j.append(name)
    surname = input("Surname : ")
    j.append(surname)
    midterm = int(input("Midterm : "))
    j.append(midterm)
    project = int(input("Project : "))
    j.append(project)
    final = int(input("Final : "))
    j.append(final)
    passingGrade = midterm * 0.3 + project * 0.3 + final * 0.4
    j.append(passingGrade)

    grade.append(passingGrade)
    student[i] = j
    
sortedGrade = grade.copy()
sortedGrade.sort(reverse=True)

for i in sortedGrade:
    a = grade.index(i)

    studentGrades.append(student.get(a))

    print("Student : ", student.get(a)[0], "Grade : ", i)

print(studentGrades)

