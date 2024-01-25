# Write your solution here
# students = {}

def add_student(students : dict, student : str):
    students[student] = [student]
    return students



def print_student(students : dict, student : str):
    if student not in students:
        print(f"{student}: no such person in the database")
        return
    print(f"{student}: \n no completed courses")
     
    
    
    
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")