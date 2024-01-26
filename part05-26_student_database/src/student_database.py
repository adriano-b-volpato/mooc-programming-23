# Write your solution here
# students = {}
def add_student(students : dict, student : str):
    students[student] = {"name": student, "courses": []}
    return students

  
def add_course(students : dict, student : str, course : tuple):
    if course[1] == 0:
        return
    for i, c in enumerate(students[student]["courses"]):
        if course[0] == c[0]:
            if c[1] < course[1]:
                students[student]["courses"][i] = course
            
            return

    students[student]["courses"].append(course)
    

def print_student(students : dict, student : str):
    if student not in students:
        print(f"{student}: no such person in the database")
        return
    
    courses = []
    sum_of_marks = 0
    for course in students[student]["courses"]:
        courses.append(course)
        sum_of_marks += course[1]
    
    if not courses:
        print(f"{student}: \n no completed courses")
        return
    print(f"{student}: ")
    print(f" {len(courses)} completed courses: ")
    for course in courses:
        avg = sum_of_marks / len(courses)
        print(f"  {course[0]} {course[1]}")
    print(f" average grade {avg} ")
    
    
    
def summary(students: dict):
    most_courses_completed = []
    best_avg = []
    for student in students:
        courses_completed = len(students[student]["courses"])
        avg = 0
        if not most_courses_completed: 
            most_courses_completed.append(courses_completed)
            most_courses_completed.append(students[student]["name"])
        if courses_completed > most_courses_completed[0]:
            most_courses_completed = []
            most_courses_completed.append(courses_completed)
            most_courses_completed.append(students[student]["name"])
        for courses in students[student]["courses"]:
            avg += courses[1]
        avg = avg/courses_completed
        if not best_avg:
            best_avg.append(avg)
            best_avg.append(students[student]["name"])
        
        if avg > best_avg[0]:
            best_avg = []
            best_avg.append(avg)
            best_avg.append(students[student]["name"])
    print(f"students {len(students)}")
    print(f"most courses completed {most_courses_completed[0]} {most_courses_completed[1]}")
    print(f"best average grade {best_avg[0]} {best_avg[1]}")
    
            

        
            


            
    
            
    
    

    
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
    
    