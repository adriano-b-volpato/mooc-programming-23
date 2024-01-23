# Write your solution here
import math



def ask_for_results():
    results = []
    
    while True:        
        inputs = input("Exam points and exercises completed: ")
        if inputs == "":
            break
        else:
            
            for item in split_inputs(inputs):
                results.append(int(item))
                
    return results

def split_inputs(string):
    result = string.split()
    return result
    

def exercises(list_results):
    exercise = []
    for i in range(1, len(list_results), 2):
        exercise.append(list_results[i])
    return exercise
    
def exersices_points(list_exercises):
    rounded_down = []
    for item in list_exercises:
        rounded_down.append(math.floor((item/10)))
    return rounded_down


def exam_points(list_results):
    pts = []
    for i in range(0, len(list_results), 2):
        pts.append(list_results[i])
    return pts

def calculate_points(exercise, exam):
    pts = []
    for i in range(len(exercise)):
        pts.append((exercise[i] + exam[i]))
    return pts

def points_avg(points):
    sum = 0
    avg = 0
    for item in points:
        sum += item
    return (sum/(len(points)))
def grading(points, exam_pts):
    fail = 0
    grade1 = 0
    grade2 = 0
    grade3 = 0
    grade4 = 0
    grade5 = 0
    for i in range(len(points)):
        if exam_pts[i] < 10:
            fail += 1
            continue
        if points[i] <=14:
            fail += 1
        if 14 < points[i] <= 17:
            grade1 += 1
        if 17 < points[i] <= 20:
            grade2 += 1
        if 20 < points[i] <= 23:
            grade3 += 1
        if 23 < points[i] <= 27:
            grade4 += 1
        if 27 < points[i] <= 30:
            grade5 += 1  
        
    
          
    return fail, grade1, grade2, grade3, grade4, grade5    
    
def pass_percentage(grading):
    fail = grading[0]
    passed = 0
    total = fail
    for i in range(1, len(grading)):
        passed += grading[i]
        total += grading[i]
         
    return (passed/total)*100

def grade_distribution(grades):
    for i in range(len(grades)-1, -1, -1):
        print(f"  {i}: {'*' * grades[i]}")
        
def statistics(pts_avg, pass_per, grades):
    print("Statistics: ")
    print(f"Points average: {pts_avg}")
    print(f"Pass percentage: {pass_per:.1f}")
    print("Grade distribution: ")
    grade_distribution(grades)
    
        

    
    
        
def main():
    inputs = ask_for_results()
    exercises_pts = exersices_points(exercises(inputs))
    exam_pts = exam_points(inputs)
    points = calculate_points(exercises_pts, exam_pts)
    grades = grading(points, exam_pts)
    
    statistics(points_avg(points), pass_percentage(grades), grades)

    

main()


