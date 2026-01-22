students = {}

def add_student(student_id, name, score):
    students[student_id] = {
        "name": name,
        "score": score,
        "grade": calculate_grade(score)
    }

def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"

def display_result():
    for student_id, details in students.items():
        print("ID:", student_id)
        print("Name:", details["name"])
        print("Score:", details["score"])
        print("Grade:", details["grade"])
        print("----------------------")

add_student("001", "John Doe", 78)
add_student("002", "Jane Smith", 62)
add_student("003", "Mike Brown", 44)

display_result()
