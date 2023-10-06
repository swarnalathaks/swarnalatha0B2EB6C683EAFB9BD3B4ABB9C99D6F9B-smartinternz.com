class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Example usage:
if __name__ == "__main__":
    students = [
        Student("Alice", "A101", 3.8),
        Student("Bob", "B102", 3.6),
        Student("Charlie", "C103", 3.9),
        Student("David", "D104", 3.5),
    ]

    sorted_students = sort_students(students)

    print("Sorted Students by CGPA (Descending Order):")
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
