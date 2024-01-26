# Write your solution here
# students = {}
def add_student(students : dict, student : str):
    students[student] = {"name": student, "courses": []}
    return students

  
def add_course(students : dict, student : str, course : tuple):
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
    
    

    
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Emily")
    print_student(students, "Peter")
    print_student(students, "Emily")
    print_student(students, "Andy")
    # students = {}
    # add_student(students, "Peter")
    # add_student(students, "Eliza")
    # print_student(students, "Eliza")
    # print_student(students, "Jack")
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))

    # print_student(students, "Peter")
    