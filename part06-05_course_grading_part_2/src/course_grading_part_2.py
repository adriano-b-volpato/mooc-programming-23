# wwite your solution here

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points_data = input("Exam points: ")
    
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points_data = "exam_points1.csv"

students = {}
exercises = {}
exam_points = {}



with open(f"{student_info}") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = parts[1], parts[2]
        
with open(f"{exercise_data}") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        grades = [int(grade) for grade in parts[1:]] #chatgpt
        exercises[parts[0]] = grades


with open(f"{exam_points_data}") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        grades = [int(grade) for grade in parts[1:]] #chatgpt
        exam_points[parts[0]] = grades



total_points = {}
  
for key, value in exercises.items():
    total = sum(value)
    total_points[key] = int((total / 40) * 10)
            
for key, value in total_points.items():
    total = sum(exam_points[key])
    total_points[key] += total


grades = {}
for key, value in total_points.items():
    grade = 0
    if 15 <= value <= 17:
        grade = 1
    if 18 <= value <= 20:
        grade = 2
    if 21 <= value <= 23:
        grade = 3
    if 24 <= value <= 27:
        grade = 4
    if 28 <= value:
        grade = 5
    grades[key] = grade
    

for key, value in students.items():
    print(f"{value[0]} {value[1]} {grades[key]}")


