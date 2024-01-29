# write your solution here

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

students = {}
exercises = {}



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


sum_exersices = {}
  
for key, value in exercises.items():
    total = sum(value)
    sum_exersices[key] = total
            


for key, value in students.items():
    print(f"{value[0]} {value[1]} {sum_exersices[key]}")











