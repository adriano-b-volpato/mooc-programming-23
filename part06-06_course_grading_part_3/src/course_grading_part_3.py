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
exercise_pts = {}
exam_points = {}
total_points = {}
grades = {}



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
        exer = [int(grade) for grade in parts[1:]] #chatgpt
        exercises[parts[0]] = exer


with open(f"{exam_points_data}") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exams = [int(grade) for grade in parts[1:]] #chatgpt
        exam_points[parts[0]] = sum(exams)




  
for key, value in exercises.items():
    total = sum(value)
    exercise_pts[key] = int((total / 40) * 10)

for key, value in exam_points.items():
    total_points[key] = value + exercise_pts[key]
    
    
            
# for key, value in total_points.items():
#     total = sum(exam_points[key])
#     total_points[key] += total


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
    






print(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}")
for key, value in students.items():
    name = f"{value[0]} {value[1]}"
    print(f"{name:30}{sum(exercises[key]):<10}{exercise_pts[key]:<10}{exam_points[key]:<10}{total_points[key]:<10}{grades[key]:<10}")
    



